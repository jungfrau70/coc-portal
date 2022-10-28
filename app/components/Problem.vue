<template>
  <div class="p-10">
    <div>
      <input
        class="input is-primary"
        type="text"
        placeholder="Search records"
        @input="onSearch"
      />
    </div>
    <button type="button" class="btn btn-info action_btn" v-on:click="downloadCSVData">
      Download
</button>
    <div class="table-container">
      <table class="table">
        <thead>
          <tr>
            <th
              v-for="(column, index) in columns"
              v-bind:key="index"
              class="border-2 p-2 text-left"
              v-on:click="sortRecords(index)"
            >
              {{ column }}
            </th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(row, index) in rows" v-bind:key="index">
            <td
              v-for="(rowItem, itemIndex) in row"
              v-bind:key="itemIndex"
              class="border-2 p-2"
            >
              {{ rowItem }}
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
// import exportFromJSON from "export-from-json";

const performSearch = (rows, term) => {
  const results = rows.filter((row) =>
    row.join(" ").toLowerCase().includes(term.toLowerCase())
  );

  return results;
};

export default {
  name: "Table",
  data() {
    return {
      term: "",
      columns: [],
      rawRows: [],
      rows: [],
      sortIndex: null,
      sortDirection: null,
    };
  },
  methods: {

    async fetchRecords() {
      const response = await axios.get('http://localhost:8000/problem/all', this.rows, {
        headers: {
          "Access-Control-Allow-Origin": "*",
          "Access-Control-Allow-Methods": "GET, POST, PATCH, PUT, DELETE, OPTIONS",
          "Access-Control-Allow-Headers": "Origin, Content-Type, X-Auth-Token"
        }
      }).then(res => {
        //console.log(res);
        this.rawRows = res
      }).catch(err => {
        console.log(err);
      });
      this.columns = Object.keys(this.rawRows.data[0]);
      this.rows = this.rawRows.data;
      //this.columns = res.data.keys()
      // this.rawRows = res.data.values()
    },
    /**
    downloadFile() {
      const data = this.rows;
      const fileName = "np-data";
      const exportType = exportFromJSON.types.csv;

      if (data) exportFromJSON({ data, fileName, exportType });
    },
    **/
    downloadCSVData() {
      let csv = 'Put,Column,Titles,Here\n';
      this.rows.forEach((row) => {
              csv += row.join(',');
              csv += "\n";
      });
  
      const anchor = document.createElement('a');
      anchor.href = 'data:text/csv;charset=utf-8,' + encodeURIComponent(csv);
      anchor.target = '_blank';
      anchor.download = 'nameYourFileHere.csv';
      anchor.click();
  },
    sortRecords(index) {
      if (this.sortIndex === index) {
        switch (this.sortDirection) {
          case null:
            this.sortDirection = "asc";
            break;
          case "asc":
            this.sortDirection = "desc";
            break;
          case "desc":
            this.sortDirection = null;
            break;
        }
      } else {
        this.sortDirection = "asc";
      }

      this.sortIndex = index;

      if (!this.sortDirection) {
        this.rows = performSearch(this.rawRows, this.term);
        return;
      }

      this.rows = this.rows.sort((rowA, rowB) => {
        if (this.sortDirection === "desc") {
          return rowB[index].localeCompare(rowA[index]);
        }

        return rowA[index].localeCompare(rowB[index]);
      });
    },
    onSearch(e) {
      this.term = e.target.value;
      this.rows = performSearch(this.rawRows, this.term);
    },
  },
  mounted() {
    this.rows = [...this.rawRows];
  },
  created() {
    this.fetchRecords();
  }
};
</script>

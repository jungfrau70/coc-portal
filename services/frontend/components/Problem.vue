<template>
  <div>
    <b-table striped small hover :items="items"></b-table>
  </div>
</template>

<!-- <template>
  <div class="p-10">
    <div>
      <input
        class="input is-primary"
        type="text"
        placeholder="Search records"
        @input="onSearch"
      />
    </div>
  </div>
</template> -->

<script>
import axios from "axios";

const performSearch = (items, term) => {
  const results = items.filter((row) =>
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
      items: [],
      sortIndex: null,
      sortDirection: null,
    };
  },
  methods: {
    async fetchRecords() {
      const response = await axios
        .get("http://localhost:8000/problem/all", this.items, {
          headers: {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods":
              "GET, POST, PATCH, PUT, DELETE, OPTIONS",
            "Access-Control-Allow-Headers":
              "Origin, Content-Type, X-Auth-Token",
          },
        })
        .then((res) => {
          // console.log(res);
          this.rawRows = res;
        })
        .catch((err) => {
          console.log(err);
        });

      // this.columns = Object.keys(this.rawRows.data[0]);
      this.items = this.rawRows.data;
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
        this.items = performSearch(this.rawRows, this.term);
        return;
      }

      this.items = this.items.sort((rowA, rowB) => {
        if (this.sortDirection === "desc") {
          return rowB[index].localeCompare(rowA[index]);
        }

        return rowA[index].localeCompare(rowB[index]);
      });
    },
    onSearch(e) {
      this.term = e.target.value;
      this.items = performSearch(this.rawRows, this.term);
    },
  },
  mounted() {
    this.items = [...this.rawRows];
  },
  created() {
    this.fetchRecords();
  },
};
</script>
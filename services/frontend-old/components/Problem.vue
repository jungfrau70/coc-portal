<template>
  <div>
    <!-- <b-form-group
      label="Selection mode:"
      label-for="table-select-mode-select"
      label-cols-md="4"
    >
      <b-form-select
        id="table-select-mode-select"
        v-model="selectMode"
        :options="modes"
        class="mb-3"
      ></b-form-select>
    </b-form-group> -->
    <b-table
      striped
      hover
      bordered
      sticky-header
      :items="rows"
      :fields="fields"
      :sort-by.sync="sortBy"
      :sort-desc.sync="sortDesc"
      responsive="xl"
    >
    </b-table>
    <b-tfoot>
      <b-tr>
        <b-td colspan="7" variant="secondary" class="text-right">
          Total Rows: <b>{{ totalRows }}</b>
        </b-td>
      </b-tr>
    </b-tfoot>
  </div>
</template>

<script>
import axios from "axios";

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
      sortBy: "id",
      sortDesc: false,
      fields: [
        { key: "id", sortable: false },
        { key: "year", sortable: true },
        { key: "month", sortable: true },
        { key: "region", sortable: true },
        { key: "az", sortable: true },
        { key: "tenant", sortable: true },
        { key: "progress", sortable: true },
        { key: "status", sortable: true },
        { key: "impact", sortable: false },
        { key: "occurred_at", sortable: false },
        { key: "title", sortable: false },
        { key: "description", sortable: false },
        { key: "action", sortable: false },
        { key: "person_in_charge", sortable: false },
        { key: "ticket_no", sortable: false },
        { key: "reviewed_at", sortable: false },
        { key: "review_desc", sortable: false },
      ],

      term: "",
      columns: [],
      rawRows: [],
      rows: [],
      sortIndex: null,
      sortDirection: null,

      totalRows: 1,
      currentPage: 1,
      perPage: 10,
      pageOptions: [10, 10, 30, { value: 100, text: "Show a lot" }],
    };
  },
  methods: {
    info(item, index, button) {
      this.infoModal.title = `Row index: ${index}`;
      this.infoModal.content = JSON.stringify(item, null, 2);
      this.$root.$emit("bv::show::modal", this.infoModal.id, button);
    },
    resetInfoModal() {
      this.infoModal.title = "";
      this.infoModal.content = "";
    },
    onFiltered(filteredItems) {
      // Trigger pagination to update the number of buttons/pages due to filtering
      this.totalRows = filteredItems.length;
      this.currentPage = 1;
    },
    async fetchRecords() {
      const response = await axios
        .get("http://localhost:8000/problem/all", this.rawRows, {
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
      this.rows = this.rawRows.data;
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

      this.rows = this.items.sort((rowA, rowB) => {
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

    // Set the initial number of items
    this.totalRows = this.rows.length;
    console.log(this.totalRows)
  },
  created() {
    this.fetchRecords();
  },
};
</script>
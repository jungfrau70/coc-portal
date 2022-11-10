<template>
  <b-table
      :items="rows"
      :fields="fields"
      :current-page="currentPage"
      :per-page="perPage"
      :filter="filter"
      :filter-included-fields="filterOn"
      :sort-by.sync="sortBy"
      :sort-desc.sync="sortDesc"
      :sort-direction="sortDirection"
      stacked="md"
      show-empty
      small
      @filtered="onFiltered"
    ></b-table>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      rawRows: [],
      items: [],
      sortBy: ["year", "month", "region", "az", "tenant", "progress", "status"],
      sortDesc: false,
      fields: [
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
      ],
      totalRows: 1,
      currentPage: 1,
      perPage: 5,
      pageOptions: [5, 10, 15, { value: 100, text: "Show a lot" }],
      sortBy: "",
      sortDesc: false,
      sortDirection: "asc",
      filter: null,
      filterOn: [],
      infoModal: {
        id: "info-modal",
        title: "",
        description: "",
      },
    };
  },
  computed: {
    sortOptions() {
      // Create an options list from our fields
      return this.fields
        .filter((f) => f.sortable)
        .map((f) => {
          return { text: f.label, value: f.key };
        });
    },
  },
  mounted() {
    this.rows = [...this.rawRows];
    // Set the initial number of items
    this.totalRows = this.items.length;
  },
  methods: {
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
    info(item, index, button) {
      this.infoModal.title = `Row index: ${index}`;
      this.infoModal.description = JSON.stringify(item, null, 2);
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
    created() {
      this.fetchRecords();
    },
  },
};
</script>


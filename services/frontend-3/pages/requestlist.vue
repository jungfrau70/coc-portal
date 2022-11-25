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
    <table class="table">
      <!-- <thead>
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
        </thead> -->
      <tbody>
        <tr v-for="(item, index) in items" v-bind:key="index">
          <td
            v-for="(rowItem, itemIndex) in item"
            v-bind:key="itemIndex"
            class="border-2 p-2"
          >
            {{ rowItem }}
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
const performSearch = (rows, term) => {
const results = rows.filter((row) =>
    row.join(" ").toLowerCase().includes(term.toLowerCase())
);

return results;
};

export default {
  name: "Request",
  data() {
    return {
      term: "",
      items: [],
      filteredItems: [],
      sortIndex: null,
      sortDirection: null,
    };
  },

  created: function () {
    this.getData();
  },

  methods: {
    async getData() {
      await axios
        .get("request/all", this.rawRows, {
          headers: {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods":
              "GET, POST, PATCH, PUT, DELETE, OPTIONS",
            "Access-Control-Allow-Headers":
              "Origin, Content-Type, X-Auth-Token",
          },
        })
        .then((res) => {
          this.rawRows = res;
        })
        .catch((err) => {
          console.log(err);
        });

      this.headers = Object.keys(this.rawRows.data[0]);
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
};
</script>

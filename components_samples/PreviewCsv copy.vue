<template>
  <div class="app">
    <div>
      <h2>Preview CSV File</h2>
      <hr />
      <label
        >File
        <input type="file" accept=".csv" @change="handleFileUpload($event)" />
      </label>
      <br />
      <table v-if="parsed" style="width: 100%">
        <thead>
          <tr>
            <th
              v-for="(header, key) in content.meta.fields"
              v-bind:key="'header-' + key"
            >
              {{ header }}
            </th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="(row, rowKey) in content.data"
            v-bind:key="'row-' + rowKey"
          >
            <td
              v-for="(column, columnKey) in content.meta.fields"
              v-bind:key="'row-' + rowKey + '-column-' + columnKey"
            >
              <input v-model="content.data[rowKey][column]" />
            </td>
          </tr>
        </tbody>
      </table>
      <br />
      <button v-on:click="submitFile()">Submit File</button>
      <button v-on:click="submitUpdates()">Submit Updates</button>
    </div>
  </div>
</template>

<script>
import Papa from "papaparse";
import axios from "axios";

export default {
  data() {
    return {
      file: "",
      content: [],
      parsed: false,
    };
  },

  methods: {
    handleFileUpload(event) {
      this.file = event.target.files[0];
      this.parseFile();
    },

    parseFile() {
      Papa.parse(this.file, {
        header: true,
        encoding: "euc-kr",
        skipEmptyLines: true,
        complete: function (results) {
          this.content = results;
          this.parsed = true;
        }.bind(this),
      });
    },

    submitFile() {
      let formData = new FormData();

      formData.append("file", this.file);

      axios
        .post("/preview-file", formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        })
        .then(function () {
          console.log("SUCCESS!!");
        })
        .catch(function () {
          console.log("FAILURE!!");
        });
    },

    submitUpdates() {
      axios
        .post("/preview-file-changes", this.content.data)
        .then(function () {
          console.log("SUCCESS!!");
        })
        .catch(function () {
          console.log("FAILURE!!");
        });
    },
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  max-width: 600px;
  margin: auto;
}
</style>

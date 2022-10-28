<template>
  <div>
    <h1>Therichpost.com</h1>
    <table class="table table-hover table-bordered" id="example">
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
</template>

<script>
//Bootstrap and jQuery libraries
import "bootstrap/dist/css/bootstrap.min.css";
import "jquery/dist/jquery.min.js";
//Datatable Modules
import "datatables.net-dt/js/dataTables.dataTables";
import "datatables.net-dt/css/jquery.dataTables.min.css";
import $ from "jquery";

import axios from "axios";
export default {
  mounted() {
    //API Call
    axios
      .get("http://localhost:8000/problem/all")
      .then((res) => {
        this.rows = res.data;
        $("#example").DataTable();
      })
      .then((res) => {
        this.rawRows = res;
      })
      .catch((err) => {
        console.log(err);
      });
    this.columns = Object.keys(this.rawRows.data[0]);
    this.rows = this.rawRows.data;
  },
  data: function () {
    return {
      columns: [],
      rawRows: [],
      rows: [],
    };
  },
};
</script>
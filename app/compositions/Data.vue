<template>
  <div>
    <button @click="add">Add new row</button><br />
    <button @click="update">Update selected rows</button><br />
    <button @click="remove">Delete selected rows</button>

    <DataTable class="display">
      <thead>
        <tr>
          <th>ID</th>
          <th>Name</th>
          <th>Email</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="user in users" :key="user.id">
          <td>{{ user.id }}</td>
          <td>{{ user.name }}</td>
          <td>{{ user.email }}</td>
        </tr>
      </tbody>
    </DataTable>
  </div>
</template>

<script>
import $ from "jquery";
import axios from "axios"; //for api calling


// DataTable.use(Select);
// DataTable.use(DataTableBs5);


export default {
  mounted() {
    //Web api calling for dynamic data and you can also use into your demo project
    axios.get("http://localhost:8000/account/1").then((res) => {
      this.users = res.data;
      setTimeout(function () {
        $("#example").DataTable({
          pagingType: "full_numbers",
          pageLength: 5,
          processing: true,
          dom: "Bfrtip",
          buttons: ["copy", "csv", "print"],
        });
      }, 1000);
    });
  },
  data: function () {
    return {
      users: [],
    };
  },
  // methods: function remove() {
  //   dt.rows({ selected: true }).every(function () {
  //     let idx = data.value.indexOf(this.data());
  //     data.value.splice(idx, 1);
  //   });
  // },
};
</script>

<style>
@import "bootstrap";
@import "datatables.net-dt";
@import "datatables.net-bs5";
</style>

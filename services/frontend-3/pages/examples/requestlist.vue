<template>
  <v-card>
    <v-dialog v-model="dialog" max-width="500px">
      <template #[`activator`]="{ on }">
        <div class="justify-space-between">
          <v-text-field
            v-model="search"
            append-icon="mdi-magnify"
            label="Search"
            single-line
            hide-details
          ></v-text-field>
          <!-- <v-btn color="primary" dark class="ml-auto ma-3" v-on="on">
              Upload
              <v-icon small>mdi-plus-circle-outline</v-icon>
            </v-btn> -->
          <v-btn color="primary" dark class="ml-auto ma-3" v-on="on">
            New Record
            <v-icon small>mdi-plus-circle-outline</v-icon>
          </v-btn>
          <v-btn
            color="primary"
            dark
            class="ml-auto ma-3"
            @click="exportData()"
          >
            Download
            <v-icon small>mdi-arrow-right-circle-outline</v-icon>
          </v-btn>
          <v-btn color="primary" dark class="ml-auto ma-3" @click="genReport()">
            Report
            <v-icon small>mdi-plus-circle-outline</v-icon>
          </v-btn>
        </div>
      </template>
    </v-dialog>
    <v-data-table
      dense
      :search="search"
      :headers="headers"
      :items="filteredDesserts"
      :options.sync="options"
      show-select
      item-key="name"
      class="elevation-1"
    >
      <template #[`body.prepend`]>
        <tr>
          <!-- <th>
              <v-icon>filter_list</v-icon>
            </th> -->

          <th v-for="header in headers" :key="header.text">
            <!-- <div v-if="filters.hasOwnProperty(header.value)"> -->
            <div>
              <v-select
                v-model="filters[header.value]"
                :items="columnValueList(header.value)"
                flat
                hide-details
                small
                multiple
                clearable
              >
              </v-select>
            </div>
            <!-- </div> -->
          </th>
        </tr>
      </template>
    </v-data-table>
  </v-card>
</template>

<script>
// import axios from 'axios'
// import { loadPyodide } from 'pyodide'

export default {
  components: {},

  data: () => ({
    options: {
      sortBy: ['name'],
      sortDesc: ['true'],
    },
    search: '',
    headers: [
      {
        text: 'Dessert (100g serving)',
        align: 'left',
        value: 'name',
      },
      { text: 'Calories', value: 'calories' },
      { text: 'Fat (g)', value: 'fat' },
      { text: 'Carbs (g)', value: 'carbs' },
      { text: 'Protein (g)', value: 'protein' },
      { text: 'Iron (%)', value: 'iron' },
    ],

    filters: {
      calories: [],
      fat: [],
      carbs: [],
    },

    desserts: [
      {
        value: false,
        name: 'Frozen Yogurt',
        calories: 159,
        fat: 6.0,
        carbs: 24,
        protein: 4.0,
        iron: '1%',
      },
      {
        value: false,
        name: 'Ice cream sandwich',
        calories: 237,
        fat: 9.0,
        carbs: 37,
        protein: 4.3,
        iron: '1%',
      },
      {
        value: false,
        name: 'Eclair',
        calories: 262,
        fat: 16.0,
        carbs: 23,
        protein: 6.0,
        iron: '7%',
      },
      {
        value: false,
        name: 'Cupcake',
        calories: 305,
        fat: 3.7,
        carbs: 67,
        protein: 4.3,
        iron: '8%',
      },
      {
        value: false,
        name: 'Gingerbread',
        calories: 356,
        fat: 16.0,
        carbs: 49,
        protein: 3.9,
        iron: '16%',
      },
      {
        value: false,
        name: 'Jelly bean',
        calories: 375,
        fat: 0.0,
        carbs: 94,
        protein: 0.0,
        iron: '0%',
      },
      {
        value: false,
        name: 'Lollipop',
        calories: 392,
        fat: 0.2,
        carbs: 98,
        protein: 0,
        iron: '2%',
      },
      {
        value: false,
        name: 'Honeycomb',
        calories: 408,
        fat: 3.2,
        carbs: 87,
        protein: 6.5,
        iron: '45%',
      },
      {
        value: false,
        name: 'Donut',
        calories: 452,
        fat: 25.0,
        carbs: 51,
        protein: 4.9,
        iron: '22%',
      },
      {
        value: false,
        name: 'KitKat',
        calories: 518,
        fat: 26.0,
        carbs: 65,
        protein: 7,
        iron: '6%',
      },
    ],

    items: [],
    currentItems: [],

    dialog: false,
    editedItem: {},
    dialogDelete: false,
    itemToDelete: {},
    // pyodide: null,
    // pyodideLoaded: null,
    output: '',
  }),
  computed: {
    filteredDesserts() {
      return this.desserts.filter((d) => {
        return Object.keys(this.filters).every((f) => {
          return this.filters[f].length < 1 || this.filters[f].includes(d[f])
        })
      })
    },
  },

  methods: {
    toggleAll() {
      if (this.selected.length) this.selected = []
      else this.selected = this.desserts.slice()
    },
    changeSort(column) {
      if (this.pagination.sortBy === column) {
        this.pagination.descending = !this.pagination.descending
      } else {
        this.pagination.sortBy = column
        this.pagination.descending = false
      }
    },
    columnValueList(val) {
      return this.desserts.map((d) => d[val])
    },
  },
}
</script>

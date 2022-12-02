<template>
  <div id="app">
    <v-app id="inspire">
      <v-data-table
        dense
        :headers="headers"
        :items="desserts"
        item-key="name"
        class="elevation-1"
        :search="search"
      >
        <template #[`body.prepend`]>
          <tr>
            <td>
              <v-text-field
                v-model="search"
                type="text"
                label="Dessert name"
              ></v-text-field>
            </td>
            <td>
              <v-text-field
                v-model="calories"
                type="number"
                label="Less than"
              ></v-text-field>
            </td>
            <td>
              <v-text-field
                v-model="fat"
                type="number"
                label="Less than"
              ></v-text-field>
            </td>
            <td>
              <v-text-field
                v-model="carbs"
                type="number"
                label="Less than"
              ></v-text-field>
            </td>
          </tr>
        </template>
      </v-data-table>
    </v-app>
  </div>
</template>

<script>
// import axios from 'axios'
// import { loadPyodide } from 'pyodide'

export default {
  components: {},

  data() {
    return {
      search: '',
      name: '',
      calories: '',
      fat: '',
      carbs: '',
      desserts: [
        {
          name: 'Frozen Yogurt',
          calories: 159,
          fat: 6.0,
          carbs: 24,
        },
        {
          name: 'Ice cream sandwich',
          calories: 237,
          fat: 9.0,
          carbs: 37,
        },
        {
          name: 'Eclair',
          calories: 262,
          fat: 16.0,
          carbs: 23,
        },
        {
          name: 'Cupcake',
          calories: 305,
          fat: 3.7,
          carbs: 67,
        },
        {
          name: 'Gingerbread',
          calories: 356,
          fat: 16.0,
          carbs: 49,
        },
        {
          name: 'Jelly bean',
          calories: 375,
          fat: 0.0,
          carbs: 94,
        },
        {
          name: 'Lollipop',
          calories: 392,
          fat: 0.2,
          carbs: 98,
        },
        {
          name: 'Honeycomb',
          calories: 408,
          fat: 3.2,
          carbs: 87,
        },
        {
          name: 'Donut',
          calories: 452,
          fat: 25.0,
          carbs: 51,
        },
        {
          name: 'KitKat',
          calories: 518,
          fat: 26.0,
          carbs: 65,
        },
      ],
    }
  },
  computed: {
    headers() {
      return [
        {
          text: 'Dessert (100g serving)',
          align: 'left',
          sortable: false,
          value: 'name',
          filter: (value) => {
            if (!this.name) return true
            return value < parseInt(this.name)
          },
        },
        {
          text: 'Calories',
          value: 'calories',
          filter: (value) => {
            if (!this.calories) return true
            return value < parseInt(this.calories)
          },
        },
        {
          text: 'Fat (g)',
          value: 'fat',
          filter: (value) => {
            if (!this.fat) return true
            return value < parseInt(this.fat)
          },
        },
        {
          text: 'Carbs (g)',
          value: 'carbs',
          filter: (value) => {
            if (!this.carbs) return true
            return value < parseInt(this.carbs)
          },
        },
      ]
    },
  },
}
</script>

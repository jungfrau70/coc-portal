<template>
  <div id="app">
    <v-app id="inspire">
      <div class="px-2">
        <h2>
          To enable server-side search to work don't pass the
          <code>search</code> prop to v-data-table
        </h2>
        <v-text-field label="search" v-model="search"></v-text-field>
        <v-data-table
          :headers="headers"
          :items="desserts"
          :options.sync="options"
          :server-items-length="totalDesserts"
          :loading="loading"
          class="elevation-4"
        >
          <template slot="items" slot-scope="props">
            <td>{{ props.item.name }}</td>
            <td class="text-xs-right">{{ props.item.calories }}</td>
            <td class="text-xs-right">{{ props.item.fat }}</td>
            <td class="text-xs-right">{{ props.item.carbs }}</td>
            <td class="text-xs-right">{{ props.item.protein }}</td>
            <td class="text-xs-right">{{ props.item.iron }}</td>
          </template>
        </v-data-table>
        <pre>{{ options }}</pre>
      </div>
    </v-app>
  </div>
</template>

<script>
// import axios from 'axios'
import {
  defineComponent,
  reactive,
  useContext,
  onMounted,
} from '@nuxtjs/composition-api'

export default {
  name: 'ProblemList',
  data() {
    return {
      search: '',
      totalDesserts: 0,
      desserts: [],
      loading: true,
      options: {},
      headers: [
        {
          text: 'Dessert (100g serving)',
          align: 'left',
          sortable: false,
          value: 'name',
        },
        { text: 'Calories', value: 'calories' },
        { text: 'Fat (g)', value: 'fat' },
        { text: 'Carbs (g)', value: 'carbs' },
        { text: 'Protein (g)', value: 'protein' },
        { text: 'Iron (%)', value: 'iron' },
      ],
    }
  },
  watch: {
    params: {
      handler() {
        // this.getDataFromApi().then((data) => {
        //   console.log('GETDATA')
        //   this.desserts = data.items
        //   this.totalDesserts = data.total
        // })
          this.desserts = data.items
          this.totalDesserts = data.total
      },
      deep: true,
    },
  },
  mounted() {
    this.getDataFromApi().then((data) => {
      this.desserts = data.items
      this.totalDesserts = data.total
    })
  },

  computed: {
    params(nv) {
      return {
        ...this.options,
        query: this.search,
      }
    },
  },

  methods: {
    getDataFromApi() {
      this.loading = true
      return new Promise((resolve, reject) => {
        const { sortBy, descending, page, rowsPerPage } = this.options
        let search = this.search.trim().toLowerCase()

        let items = this.getDesserts()

        if (search) {
          items = items.filter((item) => {
            return Object.values(item).join(',').toLowerCase().includes(search)
          })
        }

        if (this.options.sortBy) {
          items = items.sort((a, b) => {
            const sortA = a[sortBy]
            const sortB = b[sortBy]

            if (descending) {
              if (sortA < sortB) return 1
              if (sortA > sortB) return -1
              return 0
            } else {
              if (sortA < sortB) return -1
              if (sortA > sortB) return 1
              return 0
            }
          })
        }

        if (rowsPerPage > 0) {
          items = items.slice((page - 1) * rowsPerPage, page * rowsPerPage)
        }

        const total = items.length

        setTimeout(() => {
          this.loading = false
          resolve({
            items,
            total,
          })
        }, 300)
      })
    },
    getDesserts() {
      return [
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
      ]
    },
  },
  computed: {},
  methods: {
    format(date) {
      date = new Date(date)
      const day = `${date.getUTCDate()}`.padStart(2, '0')
      const month = `${date.getUTCMonth() + 1}`.padStart(2, '0')
      const year = date.getFullYear()
      return `${month}/${day}/${year}`
    },
  },
  watch: {},
}
</script>

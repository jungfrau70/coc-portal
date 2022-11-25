<template>
  <v-main class="container align-center px-1">
    <h2 class="font-weight-light mb-2">Problem List</h2>
    <v-card>
      <v-card-title>
        <v-text-field
          v-model="search"
          append-icon="mdi-magnify"
          label="Search"
          single-line
          hide-details
        ></v-text-field>
      </v-card-title>

      <v-data-table
        :search="search"
        :headers="headers"
        :items="items"
        mobile-breakpoint="800"
        class="elevation-0"
      >
        <template #[`item.actions`]="{ item }">
          <div class="text-truncate">
            <v-icon
              small
              class="mr-2"
              color="primary"              
              @click="showEditDialog(item)"
            >
              mdi-pencil
            </v-icon>
            <v-icon small color="pink" @click="showDeleteDialog(item)" >
              mdi-delete
            </v-icon>
          </div>
        </template>
        <template #[`item.details`]="{ item }">
          <div class="text-truncate" style="width: 180px">
            {{ item.Details }}
          </div>
        </template>
        <template #[`item.url`]="{ item }">
          <div class="text-truncate" style="width: 180px">
            <a :href="item.URL" target="_new">{{ item.URL }}</a>
          </div>
        </template>
      </v-data-table>
      <!-- delete dialog -->
      <v-dialog v-model="dialogDelete" max-width="500px">
        <v-card>
          <v-card-title>Delete</v-card-title>
          <v-card-text
            >Weet je zeker dat je `{{ itemToDelete.Name }}` wenst te
            verwijderen?</v-card-text
          >
          <v-card-actions>
            <v-btn color="primary" text @click="dialogDelete = false"
              >Close</v-btn
            >
            <v-btn color="primary" text @click="deleteItem()">Delete</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
      <!-- this dialog is used for both create and update -->
      <v-dialog v-model="dialog" max-width="500px">
        <template #activator="{ on }">
          <div class="d-flex">
            <v-btn color="primary" dark class="ml-auto ma-3" v-on="on">
              New
              <v-icon small>mdi-plus-circle-outline</v-icon>
            </v-btn>
          </div>
        </template>
        <v-card>
          <v-card-title>
            <span v-if="editedItem.id">Edit {{ editedItem.id }}</span>
            <span v-else>Create</span>
          </v-card-title>
          <v-card-text>
            <v-row>
              <v-col cols="12" sm="4">
                <v-text-field
                  v-model="editedItem.Name"
                  label="Name"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="8">
                <v-text-field
                  v-model="editedItem.Details"
                  label="Details"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="12">
                <v-text-field
                  v-model="editedItem.URL"
                  label="URL"
                ></v-text-field>
              </v-col>
            </v-row>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="blue darken-1" text @click="showEditDialog()"
              >Cancel</v-btn
            >
            <v-btn color="blue darken-1" text @click="saveItem(editedItem)"
              >Save</v-btn
            >
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-card>
  </v-main>
</template>

<script>
import axios from 'axios'
const apiToken = "keyZIIVNiQPvozEWb"

export default {
  data() {
    return {
      search: '',
      headers: [
        { text: 'Id', value: 'id' },
        { text: 'Year', value: 'year' },
        { text: 'Month', value: 'month', sortable: true },
        { text: 'Region', value: 'region', sortable: true },
        { text: 'Tenant', value: 'tenant', sortable: true },
        { text: 'Progress', value: 'progress', sortable: true },
        { text: 'Status', value: 'status', sortable: true },
        { text: 'Title', value: 'title', sortable: true },
        {
          text: 'Description',
          value: 'description',
          sortable: true,
          width: '180',
        },
      ],
      items: [],
      dialog: false,
      editedItem: {},
      dialogDelete: false,
      itemToDelete: {},
    }
  },
  mounted() {
    this.loadItems()
  },
  methods: {
    showEditDialog(item) {
      this.editedItem = item || {}
      this.dialog = !this.dialog
    },
    loadItems() {
      this.items = []
      axios
        .get('http://localhost:8000/problem/all', {
          headers: {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods':
              'GET, POST, PATCH, PUT, DELETE, OPTIONS',
            'Access-Control-Allow-Headers':
              'Origin, Content-Type, X-Auth-Token',
          },
        })
        .then((response) => {
          this.items = response.data.map((item) => {
            return {
              id: item.id,
              year: item.year,
              month: item.month,
              region: item.region,
              tenant: item.tenant,
              progress: item.progress,
              status: item.status,
              title: item.title,
              description: item.description,
            }
          })
        })
        .catch((error) => {
          console.log(error)
        })
    },
    saveItem(item) {
      /* this is used for both creating and updating API records
         the default method is POST for creating a new item */

      let method = 'post'
      let url = `http://localhost:8000/problem`
      const id = item.id

      // airtable API needs the data to be placed in fields object
      const data = {
        fields: item,
      }

      if (id) {
        // if the item has an id, we're updating an existing item
        method = 'patch'
        url = `http://localhost:8000/problem/${id}`

        // must remove id from the data for airtable patch to work
        delete data.fields.id
      }

      // save the record
      axios[method](url, data, {
        headers: {
          Authorization: 'Bearer ' + apiToken,
          'Content-Type': 'application/json',
        },
      }).then((response) => {
        if (response.data && response.data.id) {
          // add new item to state
          this.editedItem.id = response.data.id
          if (!id) {
            // add the new item to items state
            this.items.push(this.editedItem)
          }
          this.editedItem = {}
        }
        this.dialog = !this.dialog
      })
    },
    deleteItem() {
      console.log('deleteItem', this.itemToDelete)
      const index = this.items.indexOf(this.itemToDelete)

      /*
        axios.delete(`https://api.airtable.com/v0/${airTableApp}/${airTableName}/${id}`,
            { headers: { 
                Authorization: "Bearer " + apiToken,
                "Content-Type": "application/json"
            }
        }).then((response) => {
            this.items.splice(index, 1)
        })
        */

      this.items.splice(index, 1)
      this.dialogDelete = false
    },
    showDeleteDialog(item) {
      this.itemToDelete = item
      this.dialogDelete = !this.dialogDelete
    },
  },
}
</script>

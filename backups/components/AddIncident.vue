<template>
  <v-card>
    <v-card-title>
      <span v-if="item.id">Edit {{ item.id }}</span>
      <span v-else>Create</span>
    </v-card-title>
    <v-card-text>
      <v-row>
        <v-col cols="12" sm="2">
          <v-text-field v-model="item.year" label="Year"></v-text-field>
        </v-col>
        <v-col cols="12" sm="2">
          <v-text-field v-model="item.month" label="Month"></v-text-field>
        </v-col>
        <v-col cols="12" sm="2">
          <v-text-field
            v-model="item.region"
            label="Region"
          ></v-text-field>
        </v-col>
        <v-col cols="12" sm="2">
          <v-text-field
            v-model="item.tenant"
            label="Tenant"
          ></v-text-field>
        </v-col>
        <v-col cols="12" sm="2">
          <v-text-field
            v-model="item.progress"
            label="Porgress"
          ></v-text-field>
        </v-col>
        <v-col cols="12" sm="2">
          <v-text-field
            v-model="item.status"
            label="Status"
          ></v-text-field>
        </v-col>
      </v-row>
      <v-spacer></v-spacer>
      <v-row>
        <v-col cols="12" sm="4">
          <v-text-field v-model="item.title" label="Title"></v-text-field>
        </v-col>
        <v-col cols="12" sm="8">
          <v-text-field
            v-model="item.description"
            label="Description"
          ></v-text-field>
        </v-col>
        <v-col cols="12" sm="12">
          <v-text-field
            v-model="item.status"
            label="Status"
          ></v-text-field>
        </v-col>
      </v-row>
    </v-card-text>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn color="blue darken-1" text @click="showEditDialog()">Cancel</v-btn>
      <v-btn color="blue darken-1" text @click="saveItem(item)"
        >Save</v-btn
      >
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  name: 'AddIncident',
  // props: {
  //   editedItem: {
  //     type: Object,
  //     default: null,
  //   },
  // },
  data() {
    return {
      item: {},
    }
  },
  // mounted() {
  //   this.loadItems()
  // },
  methods: {
    // loadItems() {
    //   this.item = this.editedItem
    //   console.log(this.editedItem)
    // },
    showEditDialog() {
      this.$emit('showEditDialog')
    },
    saveItem(item) {
      this.$emit('saveItem', item)
    },
  },
}
</script>

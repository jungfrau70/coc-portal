<template>
  <v-row justify="center">
    <v-dialog transition="dialog-bottom-transition" max-width="1200">
      <template #[`activator`]="{ on, attrs }">
        <v-btn color="primary" v-bind="attrs" v-on="on">ADD</v-btn>
      </template>

      <template #[`default`]="dialog = false">
        <v-toolbar color="primary" dark>Create Record</v-toolbar>
        <v-card-text>
          <ProductDetail
            v-for="(product, i) in products"
            :key="i"
            :product="product"
          />
        </v-card-text>
        <v-card-actions class="justify-end">
          <v-btn text @click="dialog.value = false">Save</v-btn>
          <v-btn text @click="dialog.value = false">Cancel</v-btn>
        </v-card-actions>
      </template>
    </v-dialog>
  </v-row>
</template>

<script>
export default {
  data() {
    return {
      // dialog: '',
      notifications: false,
      sound: true,
      widgets: false,
      menu: ['HOME', 'ABOUT', 'PRODUCTS', 'ETC'],
      products: [
        {
          id: '0',
          title: 'Sample Product1',
          price: 10000,
        },
        {
          id: '1',
          title: 'Sample Product2',
          price: 50000,
        },
        {
          id: '2',
          title: 'Sample Product3',
          price: 30000,
        },
        {
          id: '3',
          title: 'Sample Product5',
          price: 70000,
        },
      ],
    }
  },
}
</script>

<style>
</style>
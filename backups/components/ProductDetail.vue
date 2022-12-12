<template>
  <v-row justify="center">
    <v-list-item>
      <v-list-item-content>
        <v-list-item-title>{{ product.title }}</v-list-item-title>
        <v-list-item-subtitle
          >Set the content filtering level to restrict apps that can be
          downloaded</v-list-item-subtitle
        >

        <v-div> {{ product.price }}</v-div>
      </v-list-item-content>
    </v-list-item>
    <!-- <v-card>
      <v-list three-line subheader class="product">
        <v-subheader>User Controls</v-subheader>
        <v-list-item>
          <v-list-item-content>
            <v-list-item-title>{{ product.title }}</v-list-item-title>
            <v-list-item-subtitle
              >Set the content filtering level to restrict apps that can be
              downloaded</v-list-item-subtitle
            >

            <v-div> {{ product.price }}</v-div>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-card> -->
  </v-row>
</template>
  
<script>
export default {
  name: 'ProductDetail',
  props: {
    product: {
      type: Object,
      default: null,
    },
  },
}
</script>
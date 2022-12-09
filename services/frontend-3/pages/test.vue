<!--UI-->
<template>
  <div>
    <ProductMenu :menu="menu" />
    <nav>
      <ul>
        <ProductDetail
          v-for="(product, i) in products"
          :key="i"
          :v-bind:product="product"
        />
      </ul>
    </nav>
  </div>
</template>

<!--Script-->
<script>
//   import Menu from './components/Menu.vue';
//   import Product from './components/Product.vue';

export default {
  name: 'App',
  components: {
    // ES6 부터 key, value의 변수명이 같을때 생략이 가능하다
    // Menu : Menu
    //   Menu,Product
  },
  data() {
    return {
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

<!--CSS-->
<style></style>

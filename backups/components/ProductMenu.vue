<template>
  <nav>
    <ul class="menu">
      <li v-for="(item, i) in menu" :key="i" class="menu--item">
        <a :href="'/' + item">{{ item }}</a>
      </li>
    </ul>
  </nav>
</template>

<script>
export default {
  name: 'ProductMenu',
  props: {
    menu: Array,
  },
}
</script>

<style>
.menu {
  display: flex;
  justify-content: center;
  padding: 10px;
  border-radius: 5px;
  background: steelblue;
  list-style: none;
}

.menu--item {
  padding: 10px;
}

.menu--item a {
  color: white;
  text-decoration: none;
}
</style>

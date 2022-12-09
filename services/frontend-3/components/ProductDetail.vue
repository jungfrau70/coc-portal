<template>
    <li class="product">
        <!-- <img :src="product.img"/> -->
        <div class="product--content">
          <h3 class="content--title">{{product.title}}</h3>
          <div class="content--price">상품가 : {{product.price}} 원</div>
        </div>
    </li>
  </template>
  
  <script>
  export default {
      name : 'ProductDetail',
      props : {
          product : Object
      }
  }
  </script>
  
  <style>
      .product {
          display : flex;
          flex-direction: row;
          justify-content: center;
          flex-wrap: wrap;
          align-items: center;
          list-style: none;
          margin : 10px;
      }
  
      .product--content { 
          margin-left : 10px;
      }
  </style>
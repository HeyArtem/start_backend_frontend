<template>
  <div class="post-list">
    <h1>Good Morning {{ username }}</h1>
    <h3>you avto: {{ useravto}}</h3>
    <h3>you age: {{ age }}</h3>
    <h2>Твоя мечта: {{ your_dream }}</h2>
    <div class="post" v-for="post in posts" :key=post.id>
      {{post.title}}
    </div>
    <div class="dishes">
      <h3>Блок с любимыми блюдами</h3>
      <div class="favorit_dishes" v-for="dish in favorit_dishes" :key=dish.id>
        <p>id блюда: {{ dish.id }} | Название блюда: {{dish.title}}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'PostList',
  props: {
    username: String,
    useravto: String,
    posts: Array,
    age: Number,
    your_dream: String,
    favorit_dishes: Array
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>

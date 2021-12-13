<template>
  <div class="home">
    Hello World
    <post-list :username='username' :useravto='useravto' :posts='posts' :age='age' :your_dream='your_dream' :favorit_dishes='favorit_dishes' />
  </div>
</template>

<script>
import PostList from '../components/PostList'

export default {

  name: 'Home',
  components: {
    PostList
  },
  data () {
    return {
      username: 'Art',
      useravto: 'BMW',
      posts: [
        { id: 1, title: 'Post 1' },
        { id: 2, title: 'Python' },
        { id: 3, title: 'Post 3 SQL' }
      ],
      your_dream: 'Python',
      age: 2,
      favorit_dishes: [
        { id: 1, title: 'Картофель с курицей' },
        { id: 2, title: 'Паста' },
        { id: 3, title: 'Пицца' }
      ]
    }
  }
}
</script>

<template>
  <table>
    <thead>
      <tr>
        <th>id</th>
        <th>titre</th>
        <th>description</th>
        <th>full text</th>
        <th>author</th>
        <th>created at</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="article in articles" :key="article.id">
        <td>{{article.id}}</td>
        <td>{{article.titre}}</td>
        <td>{{article.description}}</td>
        <td>{{article.full_text}}</td>
        <td>{{article.author}}</td>
        <td>{{article.created_at}}</td>

      </tr>
    </tbody>
  </table>

</template>

<script>
import axios from 'axios'
export default {
  name: 'Articles',
  data: () => {
    return {
      articles: []
    }
  },
  mounted () {
    this.getArticles()
  },
  methods: {
    getArticles() {
      const token = this.$store.state.token
      
      axios
      .get("/api/articles/")
      .then(response => {
        console.log(response)
        this.articles = response.data
      })
      .catch(error => {
        console.log(JSON.stringify(error))
      })
    }
  },
}
</script>

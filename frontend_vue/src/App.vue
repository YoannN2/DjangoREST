<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/articles">Articles</router-link> |
      <router-link to="/about">About</router-link>
    </div>
    <router-view/>

    <div v-if="authorized">
      <p>You are authorized</p>
    </div>
    <div v-else="authorized">
      <p>You are not authorized</p>
    </div>

  </div>

</template>

<script>
import axios from 'axios'

export default {
  name: 'App',
  beforeCreate () {
    this.$store.commit('initializeStore')

    const token = this.$store.state.token

    if (token) {
      axios.defaults.headers.common["Authorization"] = `Token ${token}`
    } else {
      axios.defaults.headers.common["Authorization"] = ""
    }
  },
  data () {
    return {
      authorized: this.$store.state.isAuthenticated
    }
  }
}
</script>

<style>
@import "../node_modules/bulma";
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>

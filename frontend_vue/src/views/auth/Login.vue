<template>
  <div class="login">

    <label for="username">Utilisateur</label>
    <input type="text" name="username" value="" v-model="username">

    <label for="password">Mot de Passe</label>
    <input type="password" name="password" value="" v-model="password">

    <button @click="login">S'identifier</button>

  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Login',
  data: () => {
    return {
      username: '',
      password: '',
    }
  },
  methods: {
    login: function () {
      axios
      .post("auth/token/login/", {username: this.username, password: this.password})
      .then(response => {
        const token = response.data.auth_token
        this.$store.commit("setToken", token)
        axios.defaults.headers.common["Authorization"] = `Token ${token}`
        localStorage.setItem("token", token)
        this.$router.push("/") // <-- Where to redirect after the login
      })
      .catch(error => {
        if (error.response) {
          for (const property in error.response.data) {
            this.errors.push(`${property}: ${error.response.data[property]}`)
          }
        } else if (error.message) {
          console.log(JSON.stringify(error.message))
        } else {
          console.log(JSON.stringify(error))
        }
      })
    }
  }
}
</script>

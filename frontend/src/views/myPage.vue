<template>
  <v-app>
    <newPost />
  </v-app>
</template>

<script>
// @ is an alias to /src
import newPost from '@/components/newPost.vue'

export default {
  name: 'Home',
  components: {
    newPost
  }
}
</script>

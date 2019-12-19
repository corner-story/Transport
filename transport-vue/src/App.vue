<template>
    <div>
      <Navbar v-if="display"></Navbar>  
      <router-view></router-view>
    </div>  
</template>


<script>
import Navbar from "./components/Navbar"

export default {
  name: 'app',
  computed: {
    display(){
      let islogin = this.$cookies.get("islogin")
      if(islogin !== null){
        return true
      }
      return false
    }
  },
  methods: {  
  },
  components: {
    Navbar
  },
}
</script>
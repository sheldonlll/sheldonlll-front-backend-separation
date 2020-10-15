import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
	  islogin:false,
	  access:null,
	  refresh:null,
	  username:null,
	  userid:null
  },
  mutations: {
	  loginOK(state,authorization){
		  state.islogin = authorization.islogin
		  state.access = authorization.access
		  state.refresh = authorization.refresh
		  state.username =  authorization.username
		  state.userid = authorization.userid
		  localStorage.setItem('access',state.access)
		  localStorage.setItem('refresh',state.refresh)
		  localStorage.setItem('username',state.username)
		  localStorage.setItem('userid',state.userid)
	  },
	  logoutOK(state){
		  localStorage.removeItem('username')
		  localStorage.removeItem('access')
		  localStorage.removeItem('refresh')
		  localStorage.removeItem('userid')
		  state.islogin = false
		  state.access = null
		  state.refresh = null
		  state.username = null
		  state.userid = null
	  }
  },
  actions: {
	  setUserInfo({commit},info){
		  commit('loginOK',info)
	  }
  },
  modules: {
  }
})

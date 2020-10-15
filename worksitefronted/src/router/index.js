import Vue from 'vue'
import VueRouter from 'vue-router'

const Login = ()=>import('@/views/Profile/Login')
const SignUp = ()=>import('@/views/Profile/SignUp')
const Settings = ()=>import('@/views/Settings')

const Home = ()=>import('@/views/Home')

const ArticleList = ()=>import('@/views/Article/ArticleList')
const ArticleDetail = ()=>import('@/views/Article/ArticleDetail')
const NewArticle = ()=>import('@/views/Article/NewArticle')
const ArticleEdit = ()=>import('@/views/Article/ArticleEdit')

const MusicList = ()=>import('@/views/Music/MusicList')
const MusicDetail = ()=>import('@/views/Music/MusicDetail')

const VideoList = ()=>import('@/views//Video/VideoList')
const VideoDetail = ()=>import('@/views/Video/VideoDetail')

const Chat = ()=>import('@/views/Chat/Chat')
const Profile = ()=>import('@/views/Profile/Profile')
const FeedBack = ()=>import('@/views/FeedBack')
Vue.use(VueRouter)

const routes = [
  {
		path: '/',
		redirect:"/home",
  },
  {
		path:'/login',
		name:'Login',
		component: Login
  },
  {
  		path:'/signup',
  		name:'SignUp',
  		component: SignUp
  },
  {
  		path:'/settings',
  		name:'Settings',
  		component: Settings
  },
  {
		path:'/home',
		name:'Home',
		component: Home
  },
  {
		path:'/article/list',
		name:'ArticleList',
		component: ArticleList,
  },
  {
		path:'/article/detail/:id',
		name:'ArticleDetail',
		component:ArticleDetail
  },
  {
		path:'/article/new',
		name:'NewArticle',
		component:NewArticle
  },
  {
		path:'/article/edit/:id',
		name:'ArticleEdit',
		component:ArticleEdit
  },
  {
		path:'/music/list',
		name:'MusicList',
		component:MusicList
  },
  {
  		path:'/music/:id',
  		name:'MusicDetail',
  		component:MusicDetail
  },
  {
		path:'/video/list',
		name:'VideoList',
		component:VideoList
  },
  {
  		path:'/video/:id',
  		name:'VideoDetail',
  		component:VideoDetail
  },
  {
  		path:'/chat',
  		name:'Chat',
  		component: Chat
  },
  {
  		path:'/profile',
  		name:'Profile',
  		component: Profile
  },
  {
  		path:'/feedback',
  		name:'FeedBack',
  		component: FeedBack
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

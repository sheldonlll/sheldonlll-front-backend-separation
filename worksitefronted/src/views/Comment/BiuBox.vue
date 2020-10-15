<template>
	<v-row>
		<v-col cols='1'>							
			<v-list-item-avatar class="myavatar">
				<v-img :src="userinfo.avatar">
				</v-img>
			</v-list-item-avatar>
		</v-col>
		<v-col cols='11'>
			<v-textarea filled :label="mylabel" v-model="commenttxt" counter="640" dense no-resize
outlined rows="2" background-color="#FAFAFA">
			</v-textarea>
		</v-col>
		<div class="btnarea">
			<v-btn depressed class="note">请友善发言</v-btn>
			<v-btn depressed class="biubtn" @click="sendcomment"><span>发射</span><v-icon right>send</v-icon></v-btn>
		</div>
	</v-row>
</template>

<script>
	import {getuserinfo} from '@/network/Profile/netProfile.js'
	import {sendcomment} from '@/network/Comment/Comment.js'
	export default{
		data(){
			return{
				commenttxt:null,
				userinfo:{
					avatar:'https://randomuser.me/api/portraits/men/83.jpg',
					username:null,
					personalsignature:null
				},
				mylabel:"欢迎评论!",
				islogin:false,
				myContentType:null,
				myObjectId:null,
				myRoot:null,
				myParent:null,
				myCommentUrl:null,
			}
		},
		inject: ['reload'], 
		mounted() {
			if(localStorage.getItem('userid')){
				this.islogin = true
				getuserinfo(localStorage.getItem('userid')).then(res => {
					this.userinfo.avatar = res.data.avatar
					this.userinfo.username = res.data.account_username
					this.mylabel = "Hi! " + this.userinfo.username + ", " + this.mylabel
				}).catch(err => {
					console.log(err)
				})
			}else{
				this.islogin = false
				this.userinfo.avatar =  "https://randomuser.me/api/portraits/men/82.jpg"
			}
			this.myContentType = this.ContentType
			this.myObjectId = this.ObjectId
			this.myRoot = this.Root
			this.myParent = this.Parent
			this.myCommentUrl = this.CommentUrl
		},
		props:{
			ContentType:{
				type:Number,
				default:0
			},
			ObjectId:{
				type:Number,
				default:0
			},
			Root:{
				type:Number,
				default:null
			},
			Parent:{
				type:Number,
				default:null
			},
			ReplyTo:{
				type:Number,
				default:null
			},
			CommentUrl:{
				type:String,
				default:"http://127.0.0.1:8000/api/c/comments/"
			},
			CommentLayer:{
				type:Object,
				default:null
			}
		},
		methods:{
			sendcomment(){
				if(!this.commenttxt){return}
				else{this.commenttxt.trim()}
				if(this.islogin){
					if(this.CommentLayer){
						this.myContentType = this.CommentLayer.get_content_type
						this.myObjectId = this.CommentLayer.id
						this.myRooot = this.CommentLayer.root
						this.myParent = this.CommentLayer.id
						this.myReplyTo = this.CommentLayer.author
					}
					sendcomment(this.myContentType, this.myObjectId, this.commenttxt, localStorage.getItem('userid'), this.myRooot, this.myParent, this.myReplyTo,this.myCommentUrl).then(res => {
						console.log(res)
						this.reload() //局部刷新
					}).catch(err => {
						console.log(err)
					})
				}else{
					alert('请登陆后评论吧')
				}
			},
		}
	}
</script>

<style scoped="scoped">
	.cutline{
		border: 1px dotted #BABABA;
	}
	.btnarea{
		display: flex;
		width: 100%;
		justify-content: space-between;
		flex-direction: row;
		background-color: #ececec;
	}
	.leftupbiu{
		display: flex;
		flex-direction: column;
	}
	.upbiu{
		display: flex;
		flex-direction: row;
	}
</style>

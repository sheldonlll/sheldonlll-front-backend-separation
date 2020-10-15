<template>
	<v-container>
	    <v-row>
			<div class="signupbox">
				<div class="title">
					<span class= "subheading orange--text font-weight-bold text-h3">Sign</span>
					<span class= "subheading grey--text font-weight-bold text-h3">up!</span>
				</div>
				<div class="inputop">
				  <form action="">
					  <label class="label">
						<input class="input" type="text" placeholder="Username" autocomplete/>
					  </label>
					  <label class="label">
						<input class="input" type="password1" placeholder="Password" autocomplete/>
					  </label>
					  <label class="label">
					  	<input class="input" type="password2" placeholder="ReInput-Password" autocomplete/>
					  </label>
					  <label class="label">
					  	<input class="input" type="Email" placeholder="Email" autocomplete/>
					  </label>
					  <label class="label">
					  	<input class="input" type="EmailCode" placeholder="EmailCode" autocomplete/>
					  </label>
					  <v-btn large class="mybtn" v-if="isshow" @click="btnclick">
						  <v-icon large>
							  lock
						  </v-icon>
					  </v-btn>
					  <v-btn large class="mybtn" v-if="!isshow" @click="btnclick">
						  <v-icon large>
							  lock_open
						  </v-icon>							
					  </v-btn>
				  </form>
				</div>
			</div>
	    </v-row>
	</v-container>
</template>
<script>
	export default{
		name:"SignUp",
		data(){
			return{
				username:null,
				password:null,
				isshow:true
			}
		},
		methods:{
			btnclick(){
				this.isshow = !this.isshow
			}
		}
	}
</script>
<style scoped="scoped">
	.signupbox{
		height: 600px;
		width: 100%;
		display: flex;
		text-align: center;
		flex-direction: column;
		justify-content: flex-start;
		align-items: center;
		box-shadow: 0px 5px 5px rgba(100,100,100,0.5);
		border-radius: 50px;
		border-top: 0.5px solid #CCCCCC;
		margin-top: 60px;
		margin-bottom: 5px;
		background-color: #f1f2f5;
	}
	.title{
		border: 5px solid #CCCCCC;
		width: 200px;
		height: 100px;
		border-radius: 50px;
		margin-top: -60px;
		text-decoration:underline;
		text-decoration-color:#CCCCCC;
	}
	.inputop{
		width: 600px;
		margin: auto;
	}
	.label{
		display: block;
		margin-bottom: 24px;
		width:100%
	}
	.input {
	  margin-right: 8px;
	  box-shadow:  inset 2px 2px 5px #BABECC, inset -5px -5px 10px #FFF;
	  width: 100%;
	  box-sizing: border-box;
	  transition: all 0.2s ease-in-out;
	  appearance: none;
	  -webkit-appearance: none;
	  border: 0;
	  outline: 0;
	  font-size:16px;
	  border-radius: 320px;
      padding: 16px;
	  background-color:#EBECF0;
	  text-shadow: 1px 1px 0 #FFF;
		
	  :focus {
	    box-shadow:  inset 1px 1px 2px #BABECC, inset -1px -1px 2px #FFF;
	  };

	}
	.mybtn{
		font-size: 16px;
		color:#555555;
		font-weight: bold;
		box-shadow:  -5px -5px 20px #FFF, 5px 5px 20px #BABECC;
		transition: all 0.2s ease-in-out;
		cursor: pointer;
		font-weight: 600px;  
	    :hover {
		   box-shadow: -2px -2px 5px #FFF, 2px 2px 5px #BABECC;
	    },
	    :active {
		 box-shadow: inset 1px 1px 2px #BABECC, inset -1px -1px 2px #FFF;
	     }
	   }
</style>
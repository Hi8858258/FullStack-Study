# Vue

## 一.vue的生命周期

![Vue 实例生命周期](https://cn.vuejs.org/images/lifecycle.png)

## 二. Vue基础

## 三. 组件化

### 3.1 组件使用的三个步骤

- 创建组件构造器
- 注册组件
- 使用组件

![image-20200627205253400](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200627205253400.png)

## 四. 脚手架

### 4.1 目录结构

![image-20200629194829730](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200629194829730.png)

- build，和config都是关于webpack的配置

命令：

![image-20200630065307688](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200630065307688.png)

运行npm run build 会到package.json里面去找![image-20200629195138815](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200629195138815.png)

然后执行build.js中的一些程序

（node可以直接执行js文件，不需要使用html然后用浏览器执行）

运行 npm run dev 会到package.json里面去找

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200629200206746.png" alt="image-20200629200206746" style="zoom:200%;" />

webpack-dev-server就是启动服务器

- node_module里面都是node的一些依赖
- src就是主要写代码的



初始化脚手架的时候，runtimeonly  和 runtime+compile选项的区别

1. 在main.js里面配置不一样
2. compile会先将template->ast->render->vdom->UI
3. runtimeonly是跳过了前两步，直接render->vdom->UI



## 五.脚手架使用

适应脚手架，首先要配置好路由映射。

如下在src文件夹下创建router文件，并创建index.js文件

```javascript
// 配置路由的相关信息
//1.先要导入这个插件
import VueRouter from 'vue-router'
import Vue from 'vue'

import Home from '../components/Home'
import About from '../components/About'

//2. 然后使用Vue.use使用这个插件
Vue.use(VueRouter)

//3. 创建router对象
// 用数组来形成路由和组件的映射关系
const routes = [
    {
        path:'',
        redirect:'/home'
    },    //这个是为了将主页重定向到home
    {
        path:'/home',
        component: Home        
    },
    {
        path:'/about',
        component: About
    },

]
const router = new VueRouter({
    // 配置路由和组件的关系
    routes,
    mode:'history'    //默认是hash路由，url中会有#
})

// 将router对象挂载到Vue实例中，才能真正起效果
export default router

```

在main.js里载入router

```javascript
import Vue from 'vue'
import App from './App.vue'
import router from './router/index'

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
  router,
}).$mount('#app')
```

然后再App.vue文件下引用创建的组件

```javascript
<template>
  <div id="app">
    <router-link to="/home">首页</router-link>      //这里的router-link也就是用来映射组件的
    <router-link to="/about">关于</router-link>
    <router-view></router-view>						//为了显示组件的内容
  </div>
</template>

<script>
export default {
  name: 'App',
  components: {
  }
}
</script>

<style>

</style>

```

### 5.1 router-link补充属性

- tag

router-link默认会被渲染成a标签，如果想要修改它的渲染，比如渲染成buttton，则只要增加tag属性就行，如下

```javascript
<router-link to="/home" tag ="button">首页</router-link>
```

- replace

增加replace属性后，浏览器的向前向后跳转会失效。浏览器内部会使用，history.replacestate方法

- active-class

  当点击router-link后，会自动给它设置一个router-link-active的class,所以我们在样式中给这个属性类赋予值，就可以改变它的样式,如下：(不需要给router-link添加额外的属性)

  active-class的作用是修改router-link-active的名字，意思就是点击这个router-link后，它添加的属性名会是active-class里面的值

  ```javascript
  <style>
    .router-link-active {
      color: red;
    }
  </style>
  ```

  通常不会去修改这个值，因为没必要。

可以自己实现router-link标签如下

```javascript
<template>
  <div id="app">
    <!-- <router-link to="/home" tag="button" replace>首页</router-link>
    <router-link to="/about" replace>关于</router-link> -->
    <button @click="bClick">首页</button>
    <button @click="cClick">关于</button>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'App',
  components: {
  },
  methods:{
    bClick(){
      this.$router.push('/home') //每个组件vue都会在底层赋予一个router属性
    },
    cClick(){
      this.$router.push('/about')
      //this.$router.replace('/about')
    }
  }
}
```

### 5.2 动态路由

先要在路由映射里面配置

```javascript
{
    path:'/user/:uerid',    //带冒号的就是动态路由
    component:User
}

```

然后再App.vue里面引用这个路由

```javascript
//一定要用动态绑定的方式，将userid拼接到后面
<router-link :to="'/user/'+userid">用户</router-link>
//再组件里面，需要定义一个data，里面放的就是userid
<script>
export default {
  name: 'App',
  components: {
  },
  methods:{

  },
  data(){
    return {
      userid:'lisi'
    }
  }
}
</script>

```

想要在user组件里面取到路由里面的动态参数，就需要使用以下的方法

```javascript
<template>
  <div>
      <h2>我是User</h2>
      <h2>{{userId}}</h2>
  </div>
</template>

<script>
export default {
    name:"User",
    computed:{
      userId(){
          //注意route的意思是当前活跃的那个路由，取的是冒号后面的那个值userid
        return this.$route.params.userid
      }
    }
}
</script>
```

### 5.3 懒加载

当打包时，javascript包会变得非常大，影响页面加载，如过我们能把不同路由对应的组件打包到不同的js文件，就可以避免这个问题。并且当前端请求的时候，组件才会被动态加载

```javascript
// import Home from '../components/Home'
// import About from '../components/About'
// import User from '../components/User'

// 懒加载
const Home = () => import('../components/Home')
const About = () => import('../components/About')
const User = () => import('../components/User')

```

### 5.4 路由的嵌套

过程：

1. 创建嵌套的组件
2. 将组件懒加载到index文件

```javascript
const HomeNews = () => import ('../components/HomeNews')
const HomeMessage = () => import ('../components/HomeMessage')
```

3. 在对应的根组件上用children数组引用路由映射

```javascript
 path:'/home',
        component: Home,
        children:[
            {
                path:"news",
                component:"Homenews"
            },
            {
                path:"message",
                component:"HomeMessage"
            }
        ]    
    },
```

4. 在首页的模板中的引用子组件，并且需要增加router-link

```javascript
<template>
  <div>
      <h2>我是首页</h2>
      <router-link to="home/news">新闻</router-link>
      <router-link to="home/message">消息</router-link>
      <router-view></router-view>
  </div>
</template>
```

### 5.5 传递参数

有两种方式：

- 动态路由

  参考User组件

- query类型

  前面的步骤与动态路由类似，也是创建组件，配置路由，然后再app.vue里面引入。区别在于

  ```javascript
  <router-link :to ="{path:'/profile',query:{name:'why',age:18}}">档案</router-link>
  ```

  会跳转下面的路由形式

  http://localhost:8080/profile?name=why&age=18

  router-link里面动态绑定了一个to属性，to 属性里面是一个对象。其实前面的to 也可以写成这样的形式,唯一的区别就是没有query：

  ```javascript
  <router-link to="/home" tag="button">首页</router-link>
  <router-link :to="{path:'/home'}" tag="button">首页</router-link>
  ```

  在profile里面取处query使用下面的

  ```javascript
  <h2>{{$route.query}}</h2>
  ```

  

  除了使用router-link直接传递参数，还可以自定义方法

  ```javascript
  <button @click="probtn">档案</button>
  
  methods:{
      probtn(){
        this.$router.push({
          path:'/profile',
          query:{
            name:'like',
            age:18
          }
        })
      }
    },
  ```

### 5.6 导航守卫

最主要的目的就是监听页面的跳转。

案例（每次跳转改变title的值）

一般我们可以使用组件的回调函数created()来改变title，如下

```javascript
export default {
    name:"Home",
    created(){
      document.title="首页"
    }
}
//利用的created函数在每个组件创建的时候都会调用的特性
```

上面的方法，要到每个组件里面取改，很麻烦。更好的办法就是使用全局导航守卫(放在index.js下面的守卫叫全局守卫，还有路由独享守卫，在路由映射里面配置的，以及组件内的守卫，写在组件内的)

```
path:'/about',
        component: About,
        meta:{
            title:"关于"
        } 

//前置钩子（前置守卫），意思就是在路由跳转之前回调的函数
router.beforeEach(function(to,from,next){
    //从from跳转到to
    document.title = to.meta.title
    next() //在beforeEach里面必须调用这个方法，如果不调用，跳转会失效
})
//所以还有后置狗子
```

说明：to其实就是路由里面的route实例，给route实例设定一个meta对象就可以直接设定每个路由的title。

但是这有一个问题，就是点击子组件homeNews和message的时候title不会改变，因为子组件里面的meta没有被设定。其实可以通过使用下面的形式来获取

```javascript
document.title = to.matched[0].meta.title
```

因为不管是父组件，还是子组件都会有个match属性，math是一个数组，索引0里面就包含meta这个属性（子组件会继承父组件的meta值）

### 5.7 view-router-keep-alive

目的：保存跳转前的路径视图缓存（一个页面跳转前后的状态一样，避免每次组件都重新渲染）

使用很简单，直接在app.vue里面

```javascript
<keep-alive>
    <router-view></router-view>
</keep-alive>
//使用这个所有组件都会被缓存
```

keep-alive的两个属性：

- include-字符串（组件名字）或正则表达式，只有匹配的组件会被缓存

- exclude-字符串或正则表达式，任何匹配的组件都不会被缓存

  ```javascript
  <keep-alive exclude="Profile,User">   //profile是组件的name,User前不能有空格，不然解析不了
        <router-view></router-view>
  </keep-alive>
  ```

## 六. TabBar设计

![image-20200704083020145](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200704083020145.png)

## 七. Promise

是一种异步编程得解决方案

```javascript
<script>
    //1.使用setTimeout
    //setTimeout(()=>{
    // console.log('hello');  
    // },1000)

    //Promise格式
    //在promise中需要传入一个函数，函数得参数resolve,reject本身也是函数
    new Promise((resolve,reject) => {
    //1. 第一次网络请求得代码
    setTimeout(()=>{
        resolve()
    },1000)
}).then(() => {
    //2. 第一次拿到结果的而代码
    console.log('helo world');
    console.log('helo world');
    console.log('helo world');

    return new Promise((resolve,reject) => {
        setTimeout(()=>{
            resolve()
        },1000)
    }).then(()=>{
        console.log('helo vue');
        console.log('helo vue');
        console.log('helo vue');
    })
})
</script>
```

new一个promise时候就相当于是构造函数，会做以下

- 1.保存一些状态信息
- 2.执行传入的参数（resolve,reject）

```javascript
new Promise((resolve,reject)=>{
    setTimeout((data)=>{
        resolve(data)        
                //网络请求拿到的数据，data可以传到then里面去进行处理
    	},1000)
	}).then((data) => {

	})
```

```javascript
new Promise((resolve,reject)=>{
    setTimeout(()=>{
        //settimeout假设是网络请求， 成功时候调用resolve
        resolve('helloword')
        //失败的时候（错误信息）调用reject
        //reject('error message')
        //1000模拟的是网络请求的延时，过了1s后再执行resolve，
        //resolve就是将数据传到then里面去，在then里面执行
        //具体的数据处理逻辑代码
    },1000)
}).then((data) => {
    console.log(data)
}).catch((err)=>{
    //catch 是处理错误的
})
```

all

```javascript
<script>
    Promise.all([
    //网络请求1
    new Promise((resolve,reject) => {
        $ajax({
            url:'url',
            success:function(data){
                resolve(data)
            }
        })
    }),
    //网络请求2
    new Promise((resolve,reject) => {
        $ajax({
            url:'ur2',
            success:function(data){
                resolve(data)
            }
        })
    }),
]).then(results => {
    //results是数组，里面是在all里面所有请求的结果
    results[0]
    results[1]
})
</script>
```

## 八.Vuex

vuex是专门为vue.js开发的状态（变量）管理工具

状态管理是什么？

其实可以看成需要把多个组件共享的变量全部存储在一个对象里面，然后将整个对象放在顶层的Vue实例中，让其他组件可以使用

什么样的状态需要放到全局？

比如说用户的登入状态（token），商品的收藏，购物车中的物品

```java
import Vue from 'vue'
import Vuex from 'vuex'

//1.安装插件
Vue.use(Vuex)

//2.创建对象
const store = new Vuex.Store({
    state:{
        counter:1000
    },
    mutations:{
        //在组件中修改counter时，需要通过整个
        //组件在使用这里面的方法的时候，要用
        //this.$store.commit('increment')
        
    },
    actions:{
        //如果有异步操作，需要通过actions然后再到mutations里
    },
    getters:{},
    modules:{}
})
//3.导出插件
export default store
```

使用mutations里的

```javascript
<script>
import helloVuex from '@/components/helloVuex'
export default {
  name: 'App',
  components:{
    helloVuex
  },
  data(){
    return{
      message:'我是组件',
    }
  },
  methods:{
    subClick(){
      this.$store.commit('decrement')
    },
    sumClick(){
      this.$store.commit('increment')
    }
  }
}
</script>
```

![image-20200705101130188](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200705101130188.png)

### 8.1 5个概念

- State

  就是用来放全局变量的

  理解单一状态树：即所有的状态，数据都放在一个store里面

  如果存在多个store，那可能管理起来很复杂

- Getters

  类似于computed,需要对数据进行处理

  ```javascript
  getters:{
      powerCounter(state){
          return state.counter ** 2
      },
      more20stu(state){
          //三个高阶函数一定要熟悉
          return state.students.filter(s=>{
              return s.age >= 20
          })
      },
      more20stuNumber(state,getters){
          return getters.more20stu.length
      },
      moreAgeStu(state){
          //可以接受前面传过来的参数，并进行数据筛选
          return function(age){
              return state.students.filter(s=>{
                  return s.age >= age
              })
          }
      }
  },
  ```

  

- Mutation

  vuex的store变量唯一的改变方式通过提交mutation，而且必须是同步方法

  mutation主要包含两部分:1.字符串的事件类型（type）2.一个回调函数（handler），该回调函数的第一个参数就是state

  ```javascript
  mutations:{
      //increment这些就是字符串的事件类型
      //方法,方法中的参数就是state
      increment(state){
          state.counter++
      },
      decrement(state){
          state.counter--
      },
      incrementCount(state,number){
          //当需要传递参数的时候，在state后面增加一个参数即可
          state.counter += number
      },
      addStu(state,student){
          //传递对象
          state.students.push(student)
      }
  
  },
  ```

  通过mutation更新:在vue组件当中绑定事件（如点击事件）,通过事件的去提交要调用的mutation方法

  ```javascript
  methods:{
      subClick(){
          this.$store.commit('decrement')
      },
      sumClick(){
           this.$store.commit('increment')
       },
      addCount(number){
          //p参数也被叫做ayload:载荷
        this.$store.commit('incrementCount',number)
      },
      addStu(student){
        const stu={id:150,name:'lhjk',age:16}
        this.$store.commit('addStu',stu)
      }
  ```

  参数提交风格

  ```java
  addCount(number){
      //p参数也被叫做ayload:载荷
      //1.普通提交
      this.$store.commit('incrementCount',number)
  },
  incrementCount(count){
      //2.特殊的方式
      this.$store.commit({
          type:'incrementDD',
          //这里的count其实是整个对象，包含type,和count
          count
      })
          
  //在index里面       
  incrementDD(state,playload){
              state.counter += playload.count
          },
  ```

  mutation响应式规则：

  1. 需要在store中初始化一些Vuex对应的规则。当在state中加入了属性，响应式系统会一直监听这些属性的变化 

     ```javascript
     //比如info 是在state中定义好的数据，如果我们去该它里面的属性值就是响应式的，但是不能给它添加新的属性，如：state.info['address'] = '洛杉矶'，这样做会让address属性加入到info中，但是不会响应式显示在页面上
     //可以使用Vue.set(state.info，‘address’,'洛杉矶')实现响应式
     //包括使用delete state.info.age也不能响应式得删除一个属性，要使用vue.delete(state.info,'age')
     info:{
         name:'kobe',
         age:40,
         height:1.98
     }
     ```

     mutation-types:可以方便在组件中使用

- Action

  action 里面可以做异步操作，类似与mutation

  ```javascript
      actions:{
          //上下文，这里得context就相当于store
          aUpdateInfo(context){
              setTimeout(()=>{
                  //由于只能通过mutation来改变属性，所以这里需要commit
                  context.commit('ChangeName')
              },1000)
          }
      },
          
          
          
      //组件里面使用dispatch来触发aUpdateInfo    
      updateInfo(){
        const newname = 'like'
        this.$store.dispatch('aUpdateInfo')
      }
  ```

  

- Module

  使用来给store分块得，如下

  ```javascript
  const moduleA = {
      state:{
          name:'adf'
      },
      mutations:{},
      actions:{},
      getters:{},
  }
  
  const store = new Vuex.Store({
      modules:{
          a:moduleA
      }
  })
  ```

  然后在组件里使用

  ```html
  <div>{{$store.state.a.name}}</div>
  注意这里不需要再stor后面跟modules
  ```

  

![image-20200705100124552](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200705100124552.png)

## 九. 网络模块封装（axios）

功能特点:

- 在浏览器中发送XMLHttpRequests请求
- 在node.js中发送http请求
- 支持Promise API
- 拦截请求和响应
- 转换请求和响应数据
- 等等

请求方式：

- axios(config) 最常用得，在config里面可以定义请求方法，如下面实例
- axios.requests(config)
- axios.get(url[,config])
- ……

最简单得使用实例：

```javascript
import axios from 'axios'
axios({
  url:'http://123.207.32.32:8000/home/multidata',
  method:'get'
}).then(res =>{
  console.log(res);
})
//axios支持promise，所以可以直接使用then函数，res就是接口中传回得数据
//axios
```

### 9.1 axios并发请求

axios.all([axios数组])

```javascript
axios.all([
  axios({
    url:'http://123.207.32.32:8000/home/multidata',
  }),
  axios({
    url:'http://123.207.32.32:8000/home/data',
    //axios会url和params拼接起来，形成http://123.207.32.32:8000/home/data？type=pop&page=1
    params:{
      type:'pop',
      page:1
    }
  })
]).then(resaults => {
  console.log(resaults)
})
```

### 9.2 axios的配置信息

可以做一些简单的配置，让我们的代码更简介

```javascript
axios.defaults.baseURL ="http://123.207.32.32:8000"
axios.defaults.timeout = 5

axios.all([ 
  axios({
    url:'/home/multidata',
  }),
  axios({
    url:'/home/data',
    //axios会url和params拼接起来，形成http://123.207.32.32:8000/home/data？type=pop&page=1
    params:{
      type:'pop',
      page:1
    }
  })
]).then(resaults => {
  console.log(resaults)
})![](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200705144837273.png)
```

![image-20200705144915490](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200705144915490.png)

### 9.3 axios实例

上面用的是axios全局对象，在实际开发中，当用户多了对服务器会造成很大压力，所以就会给不同ip地址发送请求数据

每个实例都有自己的配置

```javascript
//创建对应的axios实例
const instance1 = axios.create({
  baseURL:'http://123.207.32.32:8000',
  timeout:500
})
instance1({
  url:'/home/multidata'
}).then(res => {
  console.log(res);
})
instance1({
  url:'/home/data',
  params:{
    type:'pop',
    page:1
  }
}).then(res => {
  console.log(res)
})

const instance2 = axios.create({
  baseURL:'http://123.123.123.123:8000',
  timeout:1000,
  
})
```

对axios的封装，在src目录下新建一个network文件夹，将axios实例放到里面去，如下

```javascript
import axios from 'axios'

export function request(config,success,failure){
    //1.创建axios实例
    const instance = axios.create({
        baseURL:'http://123.207.32.32:8000',
        timeout:1000,
    })

    //发送网络请求，then后面是请求成功后的函数，res代表拿到的请求数据
    instance(config).then(res => {
        success(res)
    }).catch(err=>{
        failure(err)
    })
}
```

然后在需要的组件里面使用，如下

```javascript
import {request} from '@/network/request';
//封装的request中有三个参数，
//第一个就是config配置
//第二个是success回调函数，也就是下面的res，通过回调函数，可以将request的数据从封装文件中拿回来
request({
  url:'/home/multidata',
},res =>{
  console.log(res);
  //如果请求不成，那么就返回错误信息
},err =>{
  console.log(err)
})
```

也可以通过promise来简化如下

```javascript
export function request(config){
    return new Promise((resolve,reject) => {
        const instance = axios.create({
            baseURL:'http://123.207.32.32:8000',
            timeout:5000
        })

        instance(config)
        .then(res => {
            resolve(res)
        })
        .catch(err => {
            reject(err)
        })
        }
    )
}


```

有一个更好的写法：因为instance本身就是promise，所以不用再去创建一个promise

```javascript
export function request(config){
    const instance = axios.create({
        baseURL:'http://123.207.32.32:8000',
        timeout:5000
    })
    return instance(config)
}
```

然后在组件里面

```javascript
import {request} from '@/network/request';
request({
  url:'/home/multidata',
}).then(res =>{
  console.log(res)
}).catch(err => {
  console.log(err)
})
```

### 9.4 axios拦截器

用于我们在每次发送请求或者得到响应后，对某些请求进行拦截

一共有4个拦截：请求成功，请求失败，响应成功，相应失败

拦截的应用：

​	1. config里面的配置不符合服务器要求，所以需要对它进行处理后再进行传送

                          2. 每次发送网络请求的时候都希望在浏览器显示一个图片(转圈)
                          3. 某些网络请求（比如登入,需要携带token）,必须携带一些特殊的信息

```javascript
export function request(config){
    //1. 创建axios实例
    const instance = axios.create({
        baseURL:'http://123.207.32.32:8000',
        timeout:5000
    })
    //2.实例请求拦截器
    instance.interceptors.request.use( config =>{
        console.log(config);
        //拿到config信息后，一定要返回config，不然就会报错
        return config
    }, err =>{
        console.log(err)
    });
    //3.实例响应拦截
    instance.interceptors.response.use(res=>{
        console.log(res)
        //拦截之后要返回，不然其他地方不能处理
        return res.data
    },err =>{
        console.log(err);
    })
    instance.interceptors.response;
    return instance(config)
}
```


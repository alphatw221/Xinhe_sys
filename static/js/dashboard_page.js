var worksheet = new Vue({
    el: '#dashboard',
    data: {
        isFetching:false,
        worksheets:[],
        dict:{},
        n:1,
        squad_select:null,
        status_select:null,
        type1_select:null,
      
    },
    created(){
        this.isFetching=true
        axios.get('/worksheet_list/')
        .then(res => {
            this.worksheets=res.data
            axios.get('/get_all_dict/')
            .then(res => {
                this.dict=res.data
                this.isFetching=false
            }).catch(err => { console.error(err);   })

        }).catch(err => { console.error(err);   })

        
    },
    methods:{
        
    }
})
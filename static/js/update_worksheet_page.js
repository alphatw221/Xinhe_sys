var worksheet = new Vue({
    el: '#update_worksheet',
    data: {
      n:1,
      worksheet:null,
      worksheet_productss:null,
      isFetching:true,
    },
    created(){
        this.isFetching=true
        const url = window.location.href
        const parts=url.split('/')
        axios.get('/worksheet_detail/'+parts[parts.length-1])
        .then(res => {
            this.worksheet=res.data
            this.isFetching=false
        }).catch(err => { console.error(err); })
        axios.get('/get_worksheet_productss/'+parts[parts.length-1])
        .then(res => {
            this.worksheet_productss=res.data
        }).catch(err => { console.error(err); })
    },
    methods:{
        new_products(){
            var n=this.n;
            var products=this.products;
            div=document.getElementById('productss_div')
            ele1 = document.createElement('input');
            ele1.onkeyup=function(){
                input = document.getElementById('code'+n).value
                e1=document.getElementById('label3'+n)
                e2=document.getElementById('label4'+n)
                e3=document.getElementById('product'+n)
                e1.innerHTML="材料:--"
                e2.innerHTML="單位:--"
                e3.value=null
                for (i = 0; i < products.length; i++) {
                  if(input==products[i].code){
                    e1.innerHTML="材料:"+products[i].name
                    e2.innerHTML="單位:"+products[i].unit
                    e3.value=products[i].id
                  }
                }
            }
            ele2 = document.createElement('input');
            ele3=document.createElement('input');
            ele3.type="hidden";
            btn=document.createElement('button');
            br=document.createElement('br');
            label1=document.createElement('label')
            label2=document.createElement('label')
            label3=document.createElement('label')
            label4=document.createElement('label');
            btn.className='btn btn-danger';
            btn.innerHTML='取消';
            label1.innerHTML='料號:';
            label2.innerHTML='數量:';
            label3.innerHTML='材料:--';
            label4.innerHTML='單位:--';

            btn.onclick=function(){
                document.getElementById('code'+n).parentNode.removeChild(document.getElementById('code'+n))
                    document.getElementById('amount'+n).parentNode.removeChild(document.getElementById('amount'+n))
                    document.getElementById('cancel_btn'+n).parentNode.removeChild(document.getElementById('cancel_btn'+n))
                    document.getElementById('br'+n).parentNode.removeChild(document.getElementById('br'+n))
                    document.getElementById('label1'+n).parentNode.removeChild(document.getElementById('label1'+n))
                    document.getElementById('label2'+n).parentNode.removeChild(document.getElementById('label2'+n))
                    document.getElementById('label3'+n).parentNode.removeChild(document.getElementById('label3'+n))
                    document.getElementById('label4'+n).parentNode.removeChild(document.getElementById('label4'+n))
                    document.getElementById('product'+n).parentNode.removeChild(document.getElementById('product'+n))
            }
            ele1.name = 'code';
            ele1.id='code'+n;
            ele2.name = 'amount';
            ele2.id='amount'+n;
            ele2.type='number';
            ele3.name='product';
            ele3.id='product'+n;

            btn.id='cancel_btn'+n;
            br.id='br'+n;
            label1.id='label1'+n;
            label2.id='label2'+n;
            label3.id='label3'+n;
            label4.id='label4'+n;

            div.appendChild(label1);
            div.appendChild(ele1);

            div.appendChild(label3);

            div.appendChild(label4);

            div.appendChild(label2);
            div.appendChild(ele2);

            div.appendChild(btn);
            
            div.appendChild(br);
            div.appendChild(ele3);
            this.n++;
        },
        submit(){
            var worksheet_id;
            axios.post('/worksheet_list/',this.worksheet_data)
            .then(res => {
                worksheet_id=res.data['data']['id']
                product_elements=document.getElementsByName('product')
                amount_elements=document.getElementsByName('amount')
                var i;
                for (i = 0; i < product_elements.length; i++) {
                    axios.post('/worksheet_products_list/',{product:product_elements[i].value,
                    amount:amount_elements[i].value,
                    worksheet:worksheet_id
                    })
                    .then(res => {
                        console.log(res);
                    })
                    .catch(err => {
                        window.alert('批料輸入錯誤')
                    })
                }
                

            })
            .catch(err => {
                window.alert('聯單新增錯誤')
            })
            
        }
    }
})
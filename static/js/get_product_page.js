var worksheet = new Vue({
    el: '#get_product_sheet',
    data: {
      get_product_sheet_data:{serial_number:null,squad:null,date:null,warehouse:null},
      n:1,
      warehouses:null,
    },
    methods:{
        new_products(){
            var n=this.n;
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
                axios.get('/get_product_with_code/',{params:{code:input}})
                .then(res => {
                    e1.innerHTML="材料:"+res.data.name
                    e2.innerHTML="單位:"+res.data.unit
                    e3.value=res.data.id
                })
            }
            ele2 = document.createElement('input');
            ele3=document.createElement('input');
            ele3.type="hidden";
            btn=document.createElement('button');
            br=document.createElement('br');
            td=document.createElement('tr');
            label1=document.createElement('label')
            label2=document.createElement('label')
            label3=document.createElement('label')
            label4=document.createElement('label')
            btn.className = 'btn btn-danger';
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
            product_elements=document.getElementsByName('product')
            amount_elements=document.getElementsByName('amount')
            data=[]
                for (i = 0; i < product_elements.length; i++) {
                    data.push({product:product_elements[i].value,
                        amount:amount_elements[i].value,
                        warehouse:this.get_product_sheet_data.warehouse
                        })
                }
            axios.post('/get_product_sheet_list/',{get_product_sheet:this.get_product_sheet_data,get_product_sheet_productss:data})
            .then(res => {
                this.export_data=res.data['data']
                this.export()
                window.alert(res.data['message'])
                
            })
            .catch(err => {
                window.alert('領貨單新增錯誤')
            })
        },
        update_warehouse(){
            this.get_product_sheet_data.warehouse=null
            axios.get('/get_squad_warehouses/'+this.get_product_sheet_data.squad)
            .then(res => {
                this.warehouses=res.data
            })
            
        },
        export(){
            var sheet=this.export_data.get_product_sheet
            var productss=this.export_data.get_product_sheet_productss

            file_name='領貨單'+sheet.serial_number+'.xlsx'
            var excel = '<table id="expoetTable">'
            excel += '<tr><th>領料單</th></tr>'
            excel += '<tr><td>單號</td><td>'+sheet.serial_number+'</td></tr>'
            excel += '<tr><td>工班</td><td>'+sheet.squad+'</td></tr>'
            excel += '<tr><td>倉庫</td><td>'+sheet.warehouse+'</td></tr>'
            excel += '<tr><td>日期</td><td>'+sheet.date+'</td></tr>'
            excel += '<tr><th>料號</th><th>料名</th><th>數量</th><th>單位</th></tr>'
            for (i=0;i<productss.length;i++){
                excel += '<tr><td>'+productss[i].code+'</td>'
                excel += '<td>'+productss[i].name+'</td>'
                excel += '<td>'+productss[i].amount+'</td>'
                excel += '<td>'+productss[i].unit+'</td></tr>'
            }
            excel+='</table>'
            var objE = document.createElement('div') // 因爲我們這裏的數據是string格式的,但是js-xlsx需要dom格式,則先新建一個div然後把數據加入到innerHTML中,在傳childNodes[0]即使dom格式的數據
            objE.innerHTML = excel
            var sheet = XLSX.utils.table_to_sheet(objE.childNodes[0], { raw: true })// 將一個table對象轉換成一個sheet對象,raw爲true的作用是把數字當成string,身份證不轉換成科學計數法
            this.openDownloadDialog(this.sheet2blob(sheet, '領貨單'), file_name)
        },
        sheet2blob(sheet, sheetName) {
            sheetName = sheetName || 'sheet1' // 不存在sheetName時使用sheet1代替
            var workbook = {
              SheetNames: [sheetName],
              Sheets: {}
            }
            workbook.Sheets[sheetName] = sheet // 生成excel的配置項
          
            var wopts = {
              bookType: 'xlsx', // 要生成的文件類型
              bookSST: false, // 是否生成Shared String Table，官方解釋是，如果開啓生成速度會下降，但在低版本IOS設備上有更好的兼容性
              type: 'binary' // 二進制格式
            }
            var wbout = XLSX.write(workbook, wopts)
            var blob = new Blob([s2ab(wbout)], {
              type: 'application/octet-stream'
            }) // 字符串轉ArrayBuffer
            function s2ab(s) {
              var buf = new ArrayBuffer(s.length)
              var view = new Uint8Array(buf)
              for (var i = 0; i != s.length; ++i) view[i] = s.charCodeAt(i) & 0xFF
              return buf
            }
            return blob
          },
          openDownloadDialog(url, saveName) {
            if (typeof url === 'object' && url instanceof Blob) {
              url = URL.createObjectURL(url) // 創建blob地址
            }
            var aLink = document.createElement('a')
            aLink.href = url
            aLink.download = saveName || '' // HTML5新增的屬性，指定保存文件名，可以不要後綴，注意，file:///模式下不會生效
            var event
            if (window.MouseEvent) event = new MouseEvent('click')
            else {
              event = document.createEvent('MouseEvents')
              event.initMouseEvent('click', true, false, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null)
            }
            aLink.dispatchEvent(event)
          }
    }
})
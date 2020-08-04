// removing player from table
//https://www.fourfront.us/blog/store-html-table-data-to-javascript-array/
// var TableData = new Array();
// $('#add_table').each(function(row, tr){
//     TableData[row]={
//         "PlayerID" : $(tr).find('td:eq(0)').text()
//         , "PlayerName" :$(tr).find('td:eq(1)').text()
//         , "Points" : $(tr).find('td:eq(2)').text()
//         , "Assists" : $(tr).find('td:eq(3)').text()
//         ,"Rebounds" : $(tr).find('td:eq(4)').text()
//     }
// });

function addvalues_one() {
    var TableData = new Array();
    $('#add_table').each(function(row,tr){
        TableData[row]={
            "ID" : $(tr).find('td:eq(0)').text()
            ,"PlayerID" : $(tr).find('td:eq(1)').text()
            , "PlayerName" :$(tr).find('td:eq(2)').text()
            , "Points" : $(tr).find('td:eq(3)').text()
            , "Assists" : $(tr).find('td:eq(4)').text()
            ,"Rebounds" : $(tr).find('td:eq(5)').text()
        }
    });
        return TableData;
    }
    

function addvalues_two() {
    var TableData = new Array();
    $('#add_table').each(function(row,tr){
        TableData[row]={
            "ID" : $(tr).find('td:eq(6)').text()
            ,"PlayerID" : $(tr).find('td:eq(7)').text()
            , "PlayerName" :$(tr).find('td:eq(8)').text()
            , "Points" : $(tr).find('td:eq(9)').text()
            , "Assists" : $(tr).find('td:eq(10)').text()
            ,"Rebounds" : $(tr).find('td:eq(11)').text()
        }
    });
        return TableData;
    }
    function addvalues_three() {
        var TableData = new Array();
        $('#add_table').each(function(row,tr){
            TableData[row]={
                "ID" : $(tr).find('td:eq(12)').text()
                ,"PlayerID" : $(tr).find('td:eq(13)').text()
                , "PlayerName" :$(tr).find('td:eq(14)').text()
                , "Points" : $(tr).find('td:eq(15)').text()
                , "Assists" : $(tr).find('td:eq(16)').text()
                ,"Rebounds" : $(tr).find('td:eq(17)').text()
            }
        });
            return TableData;
        }

    

function Insert_Data(TableData) {
    var table = document.getElementById("del_table");
    var tr="";
    TableData.forEach(x=>{
       tr+='<tr>';
       tr+='<td>'+x.ID+'<td>'+x.PlayerID+'</td>'+'<td>'+x.PlayerName+'</td>'+'<td>'+x.Points+'</td>'+'<td>'+x.Assists+'</td>'+'<td>'+x.Rebounds+'</td>'
       tr+='</tr>'
  
    })
    table.innerHTML+=tr;
 
  } 
// function Insert_Data() {
//     var table = document.getElementById("del_table");
//     var tr="";
//     TableData.forEach(x=>{
//        tr+='<tr>';
//        tr+='<td>'+x.PlayerID+'</td>'+'<td>'+x.PlayerName+'</td>'+'<td>'+x.Points+'</td>'+'<td>'+x.Assists+'</td>'+'<td>'+x.Rebounds+'</td>'
//        tr+='</tr>'
  
//     })
//     table.innerHTML+=tr;
//     //Help......  
//   } 
//  TableData.shift();  // first row is the table header - so remove

function delrow_one() {
    var index, table = document.getElementById('del_table');
      for(var i = 1; i < table.rows.length; i++)
      {
          table.rows[2].cells[5].onclick = function()
          {
              var c = confirm("Do you want to remove this player?");
              if(c === true)
              {
                //   index = this.parentElement.rowIndex;
                //   table.deleteRow(index);
                // var tr="null";
                var tr="";
                tr +='<tr>';
                tr+='<td>'+"null"+'<td>'+"null"+'</td>'+'<td>'+"null"+'</td>'+'<td>'+"null"+'</td>'+'<td>'+"null"+'</td>'+'<td>'+"null"+'</td>'
                tr+='</tr>'
                table.rows[2].innerHTML = "";
                table.rows[2].innerHTML = tr;
              }

              
              //console.log(index);
          };
          
        }
    }
    function delrow_two() {
        var index, table = document.getElementById('del_table');
          for(var i = 1; i < table.rows.length; i++)
          {
              table.rows[3].cells[5].onclick = function()
              {
                  var c = confirm("Do you want to remove this player?");
                  if(c === true)
                  {
                    //   index = this.parentElement.rowIndex;
                    //   table.deleteRow(index);
                    // var tr="null";
                    var tr="";
                    tr +='<tr>';
                    tr+='<td>'+"null"+'<td>'+"null"+'</td>'+'<td>'+"null"+'</td>'+'<td>'+"null"+'</td>'+'<td>'+"null"+'</td>'+'<td>'+"null"+'</td>'
                    tr+='</tr>'
                    table.rows[3].innerHTML = "";
                    table.rows[3].innerHTML = tr;
                  }
    
                  
                  //console.log(index);
              };
              
            }
        }
        function delrow_three() {
            var index, table = document.getElementById('del_table');
              for(var i = 1; i < table.rows.length; i++)
              {
                  table.rows[4].cells[5].onclick = function()
                  {
                      var c = confirm("Do you want to remove this player?");
                      if(c === true)
                      {
                        //   index = this.parentElement.rowIndex;
                        //   table.deleteRow(index);
                        // var tr="null";
                        var tr="";
                        tr +='<tr>';
                        tr+='<td>'+"null"+'<td>'+"null"+'</td>'+'<td>'+"null"+'</td>'+'<td>'+"null"+'</td>'+'<td>'+"null"+'</td>'+'<td>'+"null"+'</td>'
                        tr+='</tr>'
                        table.rows[4].innerHTML = "";
                        table.rows[4].innerHTML = tr;
                      }
        
                      
                      //console.log(index);
                  };
                  
                }
            }
            function delrow_four() {
                var index, table = document.getElementById('del_table');
                  for(var i = 1; i < table.rows.length; i++)
                  {
                      table.rows[5].cells[5].onclick = function()
                      {
                          var c = confirm("Do you want to remove this player?");
                          if(c === true)
                          {
                            //   index = this.parentElement.rowIndex;
                            //   table.deleteRow(index);
                            // var tr="null";
                            var tr="";
                            tr +='<tr>';
                            tr+='<td>'+"null"+'<td>'+"null"+'</td>'+'<td>'+"null"+'</td>'+'<td>'+"null"+'</td>'+'<td>'+"null"+'</td>'+'<td>'+"null"+'</td>'
                            tr+='</tr>'
                            table.rows[5].innerHTML = "";
                            table.rows[5].innerHTML = tr;
                          }
            
                          
                          //console.log(index);
                      };
                      
                    }
                }
                function delrow_five() {
                    var index, table = document.getElementById('del_table');
                      for(var i = 1; i < table.rows.length; i++)
                      {
                          table.rows[6].cells[5].onclick = function()
                          {
                              var c = confirm("Do you want to remove this player?");
                              if(c === true)
                              {
                                //   index = this.parentElement.rowIndex;
                                //   table.deleteRow(index);
                                // var tr="null";
                                var tr="";
                                tr +='<tr>';
                                tr+='<td>'+"null"+'<td>'+"null"+'</td>'+'<td>'+"null"+'</td>'+'<td>'+"null"+'</td>'+'<td>'+"null"+'</td>'+'<td>'+"null"+'</td>'
                                tr+='</tr>'
                                table.rows[6].innerHTML = "";
                                table.rows[6].innerHTML = tr;
                              }
                
                              
                              //console.log(index);
                          };
                          
                        }
                    }
                    function delrow_six() {
                        var index, table = document.getElementById('del_table');
                          for(var i = 1; i < table.rows.length; i++)
                          {
                              table.rows[7].cells[5].onclick = function()
                              {
                                  var c = confirm("Do you want to remove this player?");
                                  if(c === true)
                                  {
                                    //   index = this.parentElement.rowIndex;
                                    //   table.deleteRow(index);
                                    // var tr="null";
                                    var tr="";
                                    tr +='<tr>';
                                    tr+='<td>'+"null"+'<td>'+"null"+'</td>'+'<td>'+"null"+'</td>'+'<td>'+"null"+'</td>'+'<td>'+"null"+'</td>'+'<td>'+"null"+'</td>'
                                    tr+='</tr>'
                                    table.rows[7].innerHTML = "";
                                    table.rows[7].innerHTML = tr;
                                  }
                    
                                  
                                  //console.log(index);
                              };
                              
                            }
                        }
                        function delrow_seven() {
                            var index, table = document.getElementById('del_table');
                              for(var i = 1; i < table.rows.length; i++)
                              {
                                  table.rows[8].cells[5].onclick = function()
                                  {
                                      var c = confirm("Do you want to remove this player?");
                                      if(c === true)
                                      {
                                        //   index = this.parentElement.rowIndex;
                                        //   table.deleteRow(index);
                                        // var tr="null";
                                        var tr="";
                                        tr +='<tr>';
                                        tr+='<td>'+"null"+'<td>'+"null"+'</td>'+'<td>'+"null"+'</td>'+'<td>'+"null"+'</td>'+'<td>'+"null"+'</td>'+'<td>'+"null"+'</td>'
                                        tr+='</tr>'
                                        table.rows[8].innerHTML = "";
                                        table.rows[8].innerHTML = tr;
                                      }
                        
                                      
                                      //console.log(index);
                                  };
                                  
                                }
                            }
                            function delrow_eight() {
                                var index, table = document.getElementById('del_table');
                                  for(var i = 1; i < table.rows.length; i++)
                                  {
                                      table.rows[9].cells[5].onclick = function()
                                      {
                                          var c = confirm("Do you want to remove this player?");
                                          if(c === true)
                                          {
                                            //   index = this.parentElement.rowIndex;
                                            //   table.deleteRow(index);
                                            // var tr="null";
                                            var tr="";
                                            tr +='<tr>';
                                            tr+='<td>'+"null"+'<td>'+"null"+'</td>'+'<td>'+"null"+'</td>'+'<td>'+"null"+'</td>'+'<td>'+"null"+'</td>'+'<td>'+"null"+'</td>'
                                            tr+='</tr>'
                                            table.rows[9].innerHTML = "";
                                            table.rows[9].innerHTML = tr;
                                          }
                            
                                          
                                          //console.log(index);
                                      };
                                      
                                    }
                                }
                                function delrow_nine() {
                                    var index, table = document.getElementById('del_table');
                                      for(var i = 1; i < table.rows.length; i++)
                                      {
                                          table.rows[10].cells[5].onclick = function()
                                          {
                                              var c = confirm("Do you want to remove this player?");
                                              if(c === true)
                                              {
                                                //   index = this.parentElement.rowIndex;
                                                //   table.deleteRow(index);
                                                // var tr="null";
                                                var tr="";
                                                tr +='<tr>';
                                                tr+='<td>'+"null"+'<td>'+"null"+'</td>'+'<td>'+"null"+'</td>'+'<td>'+"null"+'</td>'+'<td>'+"null"+'</td>'+'<td>'+"null"+'</td>'
                                                tr+='</tr>'
                                                table.rows[10].innerHTML = "";
                                                table.rows[10].innerHTML = tr;
                                              }
                                
                                              
                                              //console.log(index);
                                          };
                                          
                                        }
                                    }
                                    function delrow_ten() {
                                        var index, table = document.getElementById('del_table');
                                          for(var i = 1; i < table.rows.length; i++)
                                          {
                                              table.rows[11].cells[5].onclick = function()
                                              {
                                                  var c = confirm("Do you want to remove this player?");
                                                  if(c === true)
                                                  {
                                                    //   index = this.parentElement.rowIndex;
                                                    //   table.deleteRow(index);
                                                    // var tr="null";
                                                    var tr="";
                                                    tr +='<tr>';
                                                    tr+='<td>'+"null"+'<td>'+"null"+'</td>'+'<td>'+"null"+'</td>'+'<td>'+"null"+'</td>'+'<td>'+"null"+'</td>'+'<td>'+"null"+'</td>'
                                                    tr+='</tr>'
                                                    table.rows[11].innerHTML = "";
                                                    table.rows[11].innerHTML = tr;
                                                  }
                                    
                                                  
                                                  //console.log(index);
                                              };
                                              
                                            }
                                        }
                                        function delrow_eleven() {
                                            var index, table = document.getElementById('del_table');
                                              for(var i = 1; i < table.rows.length; i++)
                                              {
                                                  table.rows[12].cells[5].onclick = function()
                                                  {
                                                      var c = confirm("Do you want to remove this player?");
                                                      if(c === true)
                                                      {
                                                        //   index = this.parentElement.rowIndex;
                                                        //   table.deleteRow(index);
                                                        // var tr="null";
                                                        var tr="";
                                                        tr +='<tr>';
                                                        tr+='<td>'+"null"+'<td>'+"null"+'</td>'+'<td>'+"null"+'</td>'+'<td>'+"null"+'</td>'+'<td>'+"null"+'</td>'+'<td>'+"null"+'</td>'
                                                        tr+='</tr>'
                                                        table.rows[12].innerHTML = "";
                                                        table.rows[12].innerHTML = tr;
                                                      }
                                        
                                                      
                                                      //console.log(index);
                                                  };
                                                  
                                                }
                                            }
                                            // function delrow_twelve() {
                                            //     var index, table = document.getElementById('del_table');
                                            //       for(var i = 1; i < table.rows.length; i++)
                                            //       {
                                            //           table.rows[i].cells[5].onclick = function()
                                            //           {
                                            //               var c = confirm("Do you want to remove this player?");
                                            //               if(c === true)
                                            //               {
                                            //                 //   index = this.parentElement.rowIndex;
                                            //                 //   table.deleteRow(index);
                                            //                 // var tr="null";
                                            //                 var tr="";
                                            //                 tr +='<tr>';
                                            //                 tr+='<td>'+"null"+'<td>'+"null"+'</td>'+'<td>'+"null"+'</td>'+'<td>'+"null"+'</td>'+'<td>'+"null"+'</td>'+'<td>'+"null"+'</td>'
                                            //                 tr+='</tr>'
                                            //                 table.rows[13].innerHTML = "";
                                            //                 table.rows[13].innerHTML = tr;
                                            //               }
                                            
                                                          
                                            //               //console.log(index);
                                            //           };
                                                      
                                            //         }
                                            //     }
                                                function delrow_twelve() {
                                                    var index, table = document.getElementById('del_table');
                                                          table.rows[13].cells[5].onclick = function()
                                                          {
                                                              var c = confirm("Do you want to remove this player?");
                                                              if(c === true)
                                                              {
                                                                //   index = this.parentElement.rowIndex;
                                                                //   table.deleteRow(index);
                                                                // var tr="null";
                                                                var tr="";
                                                                tr +='<tr>';
                                                                tr+='<td>'+"null"+'<td>'+"null"+'</td>'+'<td>'+"null"+'</td>'+'<td>'+"null"+'</td>'+'<td>'+"null"+'</td>'+'<td>'+"null"+'</td>'
                                                                tr+='</tr>'
                                                                table.rows[13].innerHTML = "";
                                                                table.rows[13].innerHTML = tr;
                                                              }
                                                
                                                              
                                                              //console.log(index);
                                                            };
                                                          
                                                        }
                    
                                                function delrow_thirteen() {
                                                    var index, table = document.getElementById('del_table');
                                                      for(var i = 1; i < table.rows.length; i++)
                                                      {
                                                          table.rows[14].cells[5].onclick = function()
                                                          {
                                                              var c = confirm("Do you want to remove this player?");
                                                              if(c === true)
                                                              {
                                                                //   index = this.parentElement.rowIndex;
                                                                //   table.deleteRow(index);
                                                                // var tr="null";
                                                                var tr="";
                                                                tr +='<tr>';
                                                                tr+='<td>'+"null"+'<td>'+"null"+'</td>'+'<td>'+"null"+'</td>'+'<td>'+"null"+'</td>'+'<td>'+"null"+'</td>'+'<td>'+"null"+'</td>'
                                                                tr+='</tr>'
                                                                table.rows[14].innerHTML = "";
                                                                table.rows[14].innerHTML = tr;
                                                              }
                                                
                                                              
                                                              //console.log(index);
                                                          };
                                                          
                                                        }
                                                    }
                                                    
                                                      
    function add_elements_one() {
        var add_table = document.getElementById('add_table');
          
              
              add_table.rows[2].cells[6].onclick = function()
              {
                  var c = confirm("Do you want to add this player?");
                  if(c === true)
                  {
                      
                      var tab = addvalues_one();   
                      Insert_Data(tab);
                      }
                  }
                  
                  //console.log(index);
              
              
            }
        
        function add_elements_two() {
            var add_table = document.getElementById('add_table');
              
                  
                  add_table.rows[3].cells[6].onclick = function()
                  {
                      var c = confirm("Do you want to add this player?");
                      if(c === true)
                      {
                          
                          var tab = addvalues_two();   
                          Insert_Data(tab);
                          }
                      }
                      
                      //console.log(index);
                  };
                  
            function add_elements_three() {
                var add_table = document.getElementById('add_table');
                  
                      
                      add_table.rows[4].cells[6].onclick = function()
                      {
                          var c = confirm("Do you want to add this player?");
                          if(c === true)
                          {
                              
                              var tab = addvalues_three();   
                              Insert_Data(tab);
                              }
                          }
                          
                          //console.log(index);
                      };
                      
                    
                

    delrow_one();
    delrow_two();
    delrow_three();
    delrow_four();
    delrow_five();
    delrow_six();
    delrow_seven();
    delrow_eight();
    delrow_nine();
    delrow_ten();
    delrow_eleven();
    delrow_twelve();
    delrow_thirteen();
    add_elements_one();
    add_elements_two();
    add_elements_three();
    
    
    //    function addr() {
    //     var tableRef = document.getElementById('add_table');
    //     var tables = document.getElementById('del_table');
        
    //       tableRef.rows[i].cells[2].onclick = function()
    //       {
    //           var c = confirm("Do you want to add this player?");
    //           if(c === true)
    //           {
    //               tables.insertRow(14);
    //           }
              
    //           //console.log(index);
    //       };
          
    //     }
    
    
    
   
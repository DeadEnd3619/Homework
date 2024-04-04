let thn = true

// $(function(){
//     $('.click').on('click',function(){
//         $('#panel1').css({
//             'background-color': 'Blue',
//             'color': 'white'
//         });$('#panel1-content').html('the background is blue and the text is white')
//         $('#panel2').css({
//             'background-color': 'Green',
//             'color': 'white'
//         });$('#panel2-content').html('the background is green and the text is white')
//         $('#panel3').css({
//             'background-color': 'DarkGrey'
//         });$('#panel3-content').html('the background is darkgrey and the text is black  and the font is monospace, including the panel contect').css({
//             'font-family': 'monospace',
//         })
//         $('#panel4').css({
//             'background-color': 'Red',
//             'color': 'white'
//         })
//     })
// });

$(function(){
    $('#button1').on('click', function(){$('#panel1').toggle()
    $('#panel4').toggle()})
    $('#button2').on('click', function(){$('#panel2').toggle();$('#panel3').toggle()
    $('#panel4').toggle()})
    $('#button3').on('click', function(){$('#panel1').toggle()
    $('#panel3').toggle()})
    $('#button4').on('click', function(){$('#panel1').toggle()
    $('#panel2').toggle()})
});
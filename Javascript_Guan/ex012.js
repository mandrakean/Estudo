var agora = new Date()
var hora = agora.getHours()
console.log(`agora são ${hora} horas.`)
if (hora < 12){
    console.log('Bom dia!')
} else if (hora > 12 && hora < 18){
    console.log('boa tarde!')
} else {
    console.log('boa noite!')
}
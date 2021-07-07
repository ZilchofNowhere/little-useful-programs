const readline = require("readline")
const rl = readline.createInterface({input: process.stdin, output: process.stdout})

rl.question("Lütfen hatırlatılmak istediğiniz şeyi girin\n", (answer)=>{
   console.log(`${answer} için kurduğunuz hatırlatıcı başlıyor...`)
   rl.question("Ne kadar süre sonra hatırlatılacağını girin (dakika cinsinden)\n", (dur)=>{
      console.log(`Hatırlatmanız ${dur} dakika sonra gerçeklecek`)
      setTimeout(() => {
         console.log(`${answer} zamanı!!!`) 
      }, parseInt(dur)*60000); // 1 dk = 60000 ms
      clearTimeout()
      if (clearTimeout) {
         rl.close()
      }
   })
})
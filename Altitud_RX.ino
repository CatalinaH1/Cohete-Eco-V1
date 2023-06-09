#include <SPI.h>
#include <RF24.h>
RF24 radio(10,8); // CE, CSN

const byte address[6] = "00001";
float ALTITUD, V_altitud;
void setup()
{ 
  Serial.begin(9600, SERIAL_8N1);
  
  radio.begin();
  radio.openReadingPipe(0, address);
  radio.setChannel(101);
  radio.setDataRate(RF24_250KBPS);
  radio.setPALevel(RF24_PA_HIGH);
  radio.startListening();

  /*Serial.println("Receptor iniciado");*/ 
}
void loop()
{
  if (radio.available())    
  {  
    float datos[1];
    radio.read(datos, sizeof(datos));
    ALTITUD = datos[0];
    Serial.println(ALTITUD);
 }
  delay(50);
}

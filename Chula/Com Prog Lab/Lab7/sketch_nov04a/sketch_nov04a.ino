#include <M5Stack.h>
void setup() {
  M5.begin();
  M5.Lcd.setTextSize(2);
  M5.Lcd.setTextColor(0xe8e4);
  Serial.println("Arduino String Lab, Exercise 2");
}
 
char buffer[80];
 
void loop() {
  Serial.print("Please enter your name (with Mr. or Ms.) \n>");
  while(!Serial.available()) { 
  }      
  Serial.readBytes(buffer,80); 
  String name=String(buffer);
  String lname = String(buffer);
  lname.toLowerCase();
  Serial.println(name);
  int pos;
  if ((pos=lname.indexOf("mr."))!=-1) {
    Serial.println("Hello mister! "+name.substring(pos+3));
    M5.Lcd.setTextColor(0x51d);
    M5.Lcd.println("Hello Mister!");
  } 
  else if ((pos=lname.indexOf("ms."))!=-1) {
    Serial.println("Hello miss! "+ name.substring(pos+3));
    M5.Lcd.setTextColor(0xe8e4);
    M5.Lcd.println("Hello Miss!");
  } 
  else {
    Serial.println("Hello there! "+ name);
    M5.Lcd.setTextColor(0x2589);
    M5.Lcd.println("Hello Master!");
  }
  Serial.println(".");
  M5.update();
}

#include <M5Stack.h>
void setup() {
  M5.begin();
  M5.Lcd.setTextSize(2);
  M5.Lcd.setTextColor(0xe8e4);
  Serial.println("Arduino String Lab, Exercise 3");
}
 
char buffer[80];
 
void loop() {
  Serial.print("Input: ");
  while(!Serial.available()) { 
  }
  Serial.readBytes(buffer,80);
  String inpt = String(buffer);
  int strlength = inpt.length();
  int charcount = 0;
  int wordcount = 1;
  for (int x = 0; x < strlength; x++) {
    if (inpt.charAt(x) == ' ') {
      wordcount = wordcount + 1;
      } else if (isAlpha(inpt.charAt(x))) {
        charcount += 1;
        }
      }
  Serial.print(wordcount);
  Serial.print(" words, ");
  Serial.print(charcount);
  Serial.print(" characters, ");
  Serial.print(strlength);
  Serial.print(" bytes");
  Serial.println("\n");
  M5.update();
  memset(buffer, 0, sizeof(buffer));
}

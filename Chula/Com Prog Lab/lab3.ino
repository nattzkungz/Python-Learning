void myInfo() {
	if (Serial.available()>0) {
		int key=Serial.read();
            if (key == '!') {
                Serial.println("Thanakrit ID: 6438084721");
                Serial.println("Tanakrit ID: 6438086021");
                Serial.println("Chanthep ID: 6438049821");
            }


}

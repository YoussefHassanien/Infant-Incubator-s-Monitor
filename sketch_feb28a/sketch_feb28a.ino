#include <DHT.h>
#define DHTPIN 2          // Digital pin connected to the DHT sensor
#define DHTTYPE DHT11     // DHT 11
#define HEARTBEAT_PIN A0  // Analog pin connected to the heartbeat sensor


DHT dht(DHTPIN, DHTTYPE);
int relayPin = 7; 
int Led = 11;

void setup() {
   // Set relay pin as output
  pinMode(relayPin, OUTPUT);
  pinMode(Led, OUTPUT);
  Serial.begin(9600);   // Initialize serial communication
  dht.begin();          // Initialize DHT sensor
}

void loop() {
  float humidity = dht.readHumidity();       // Read humidity value from DHT sensor
  float temperature = dht.readTemperature(); // Read temperature value from DHT sensor
  

  // Read heartbeat sensor value
  int heartbeat = analogRead(HEARTBEAT_PIN);
  heartbeat = map(heartbeat, 0, 1023, 0, 255);
  // Check if any reads failed and exit early (to try again).
  if (isnan(humidity) || isnan(temperature)) {
    return;
  }

  if (temperature<28)
  {
    digitalWrite(relayPin, HIGH);
  } 
  else if (temperature>=26)
  {
    digitalWrite(relayPin, LOW);
  }

 if (Serial.available() > 0) {
    char jaundice_signal = Serial.read();
    if (jaundice_signal == '1') {
      digitalWrite(Led, HIGH); // Turn on the LED
    } 
    else if (jaundice_signal == '2')
    {
      digitalWrite(Led, LOW); // Turn of the LED
    }
  }
  

  // Print temperature, humidity, and heartbeat values
  Serial.print(humidity);
  Serial.print(",");
  Serial.print(temperature);
  Serial.print(",");
  Serial.println(heartbeat);

  delay(500);
}


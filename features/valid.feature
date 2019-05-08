Feature: Paid valid

Scenario: Data Valid 
Given: go to page kitabisa
And: click navbar Donasi
And: choose one item 
And: click button donasi sekarang
When: input paid 
And: click button pilih methode paid
And: click choose methode
And: input Nama 
And: Input email or WhatsApp
And: input comment
Then: i should see redirect paid 
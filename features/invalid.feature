Feature: Paid invalid

Scenario: Data invalid 
Given: go to page url
And: navbar Donasi
And: pilih one item 
And: click button donasi now
When: input paid less than 100
And: button pilih methode paid
And: choose methode
And: masukkan Nama 
And: masukkan email or WhatsApp
And: masukkan comment
Then: i see redirect paid 
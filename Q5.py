# Name: Ida Bagus Ryogassa Avatara (Ryo)
# Teacher: Mr Jude
# Class: Intro to Programming L1AC

print("Wavelength Calculator")
inputVelocity = float(input('Enter a Value of Speed (m/s): '))
inputFrequency = float(input('Enter a Value for Frequency (Hz): '))

# Lambda = v/f
getWavelength = inputVelocity / inputFrequency
print()
print("The Speed (m/s): ", inputVelocity)
print("The Frequency(Hz): ", inputFrequency)
print("The Wavelength (m): ", getWavelength)

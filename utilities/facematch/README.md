# Face++ to identify a person 
#download github code
```
$git clone https://github.com/lbaitemple/facematch.git
$cd facematch
```


#install picamera on raspberry pi
```
$sudo apt-get update
$sudo apt-get upgrade

$sudo apt-get install python-picamera python3-picamera
```

# make sure you create pictures 
```
$mkdir -p test/pictures_faces
$cp someone.jpg /test/pictures_faces
```

# how to run the code
```
$python  rpi_pic_comp.py 
```


#### possible run time error
###### If you get camera turn into red and nothing happens, "No data received from sensor. Check all connections...", please 
### make sure you use a USB cable which can supply 250mA current.

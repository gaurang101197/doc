# Windows 10

## Creating bootable USB

### Using MAC

https://www.youtube.com/watch?v=YkvLkRxPTB4

[Create a bootable Windows 10 installation USB on macOS](https://jensd.be/1349/windows/create-a-bootable-windows-10-installation-usb-on-macos)

- **Main steps**
    - Click on ISO file, it will be mounted with `CCCOMA_X64FRE_EN-US_DV9` name most probably.
    - Format USB as “`MS-DOS (FAT)`” and “`Master Boot Record`” as scheme
    - As FAT can read max 4GB file size, so run below command to split the `install.wim` file whose size is more than 4GB.
        
        ```bash
        #brew install wimlib
        #wimlib-imagex split /Volumes/CCCOMA_X64FRE_EN-US_DV9/sources/install.wim /Volumes/WINUSB/sources/install.swm 4000
        ```
        

### Activating windows 10 Home

[Windows 10 Product Keys For All Versions 32bit+64bit (2022)](https://www.blowingideas.com/windows-10-product-keys/)

Run below commands in CMD in `administration` mode

```powershell
slmgr.vbs /ipk TX9XD-98N7V-6WMQ6-BX7FG-H8Q99
slmgr /skms kms8.msguides.com
slmgr.vbs /ato
```

### Downloading required Drivers

- You can download the [intel driver and support assistant](https://www.intel.com/content/www/us/en/support/detect.html) which will automatically detect the drivers needs to update.
- You can manually search for the intel device you are using [here](https://www.intel.com/content/www/us/en/download-center/home.html). And download the required drivers from there.

### Download required software

- firefox
- VLC
- liber office
- intel driver management
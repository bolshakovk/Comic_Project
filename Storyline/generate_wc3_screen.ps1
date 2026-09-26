Add-Type -AssemblyName System.Drawing

$sourceImagePath = 'C:\Users\bolsh\.gemini\antigravity\brain\ac323aa2-4fed-4b1f-9644-c337e40e4da2\media__1777220127908.jpg'
$outputImagePath = '.\wc3_loading_screen_edited.png'

$img = [System.Drawing.Image]::FromFile($sourceImagePath)
$bmp = New-Object System.Drawing.Bitmap($img)
$g = [System.Drawing.Graphics]::FromImage($bmp)
$g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias

$destRect = New-Object System.Drawing.Rectangle(500, 310, 480, 150)
$brushColor = [System.Drawing.Color]::FromArgb(210, 35, 30, 20)
$brush = New-Object System.Drawing.SolidBrush($brushColor)
$g.FillRectangle($brush, $destRect)

$fontFamily = New-Object System.Drawing.FontFamily("Georgia")
$font = New-Object System.Drawing.Font($fontFamily, 13, [System.Drawing.FontStyle]::Regular)

$textColor = [System.Drawing.Color]::FromArgb(255, 255, 214, 133)
$textBrush = New-Object System.Drawing.SolidBrush($textColor)

$format = New-Object System.Drawing.StringFormat()
$format.Alignment = [System.Drawing.StringAlignment]::Center
$format.LineAlignment = [System.Drawing.StringAlignment]::Center

$text = "все началось с хаствуда, который рубил деревья на столько яростно, что придя в дом, он зарубил свою семью, он долго горевал, но черный алмаз нашел его, на землях вов сируса начался коричневый поход..."

$shadowBrush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::Black)
$shadowRect = New-Object System.Drawing.Rectangle($destRect.X + 2, $destRect.Y + 2, $destRect.Width, $destRect.Height)
$g.DrawString($text, $font, $shadowBrush, $shadowRect, $format)

$g.DrawString($text, $font, $textBrush, $destRect, $format)

$g.Dispose()
$bmp.Save($outputImagePath, [System.Drawing.Imaging.ImageFormat]::Png)
$bmp.Dispose()
$img.Dispose()

Write-Output "Done"

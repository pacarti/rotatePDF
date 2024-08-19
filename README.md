<h1>rotatePDF</h1>

<p>Rotates the given page(or pages) of a PDF file with a chosen angle(90, 180, 270).</p> <br><br>

<h2>Single-page PDF file</h2> 
<p>Syntax:<br> <code>./rotatePDF [PDF file] [rotation angle]</code>
<p>For example: <br>
<code>./rotatePDF myFile.pdf 90</code></p>

<br><br>

<h2>Multiple-page PDF files</h2>

<p>You can rotate the pages in 3 modes:</p>

  <h3>Single page:</h3>
  <p>Syntax:<br> <code>./rotatePDF [PDF file] [page number to be rotated] [Angle]</code></p>
  <p>For example: <br>
  <code>./rotatePDF myFile.pdf 2 90</code><br></p>
  <br>
  <h3>Multiple given pages:</h3>
  <p>Syntax:<br> <code>./rotatePDF [PDF file] '[page numbers to be rotated separated by comma]' [Angle]</code></p>
  <p>For example: <br>
  <code>./rotatePDF myFile.pdf '[1, 2, 3]' 90</code><br></p>
  <br>
  <h3>Pages scope to be rotated:</h3>
  <p>Syntax:<br> <code>./rotatePDF [PDF file] '[A-B scope of pages separated by dash]' [Angle]</code></p>
  <p>For example: <br>
  <code>./rotatePDF myFile.pdf '[1-3]' 90</code></p>


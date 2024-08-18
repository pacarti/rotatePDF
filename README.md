<h1>rotatePDF</h1>

<p>Rotates the given page(or pages) of a PDF file with a chosen angle(90, 180, 270).</p> <br><br>
<p>You can rotate the pages in 3 modes:</p>
<ul>
  <li>Single page:
  <p>Syntax: <code>./rotatePDF [PDF file] [page number to be rotated] [Angle]</code></p>
  <p>For example: </p>
  <code>./rotatePDF myFile.pdf 2 90</code></li><br>
  <li>Multiple given pages:
  <p>Syntax: <code>./rotatePDF [PDF file] '[page numbers to be rotated separated by comma]' [Angle]</code></p>
  <p>For example: </p>
  <code>./rotatePDF myFile.pdf '[1, 2, 3]' 90</code></li><br>
  <li>Pages scope to be rotated:
  <p>Syntax: <code>./rotatePDF [PDF file] '[A-B scope of pages separated by dash]' [Angle]</code></p>
  <p>For example: </p>
  <code>./rotatePDF myFile.pdf '[1-3]' 90</code></li>
</ul>

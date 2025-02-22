<?xml version="1.0"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
	<xsl:template match="/">
		<html>
		<head>
		<style>
			body  {font-family: Trebuchet MS; font-size: 10pt; }
			table {font-family: Trebuchet MS; font-size: 10pt; }
			h2	{font-family: Trebuchet MS; font-weight:bold; font-size: 14pt; color: #000000; }
			tr	{background-color: #f0f0f0;}
			tr.caption {background-color: #cccccc}
		</style>
		</head>
		<body>
 		<h1>PDF/A Validation Results (Before Conversion):</h1>
		<h2>Run DateTime: <xsl:value-of select="PDFAManagerReport/@RunDateTime"/></h2>
 		<h2>Fail:</h2>
 		  <xsl:for-each select="PDFAManagerReport/Validation/Fail">
 		  <div style="border: solid darkred 1px;">
 		  <table width="100%">
				<tr>
				  <td><xsl:text disable-output-escaping="yes">&lt;a href=&quot;</xsl:text><xsl:value-of select="@FileNameAndPath"/><xsl:text disable-output-escaping="yes">&quot;&gt;</xsl:text><xsl:value-of select="@FileName"/><xsl:text disable-output-escaping="yes">&lt;/a&gt;</xsl:text></td>
				</tr>
			</table>
  			<table width="100%">
			  <tr class="caption">
			    <td width="10%"><I>Error ID</I></td>
			    <td width="70%"><I>Message</I></td>
			    <td width="20%"><I>Obj Refs</I></td>
			  </tr>
			  <xsl:for-each select="Error">
				  <tr>
				    <td><xsl:value-of select="@Code"/></td>
				    <td><xsl:value-of select="@Message"/></td>
				    <td><xsl:value-of select="@Refs"/></td>
				</tr>
  	    </xsl:for-each>
			</table>
			</div>
			<br/>
		</xsl:for-each>
 		<h2>Pass:</h2>
	  <div style="border: solid darkblue 1px;">
		<table width="100%">
		<xsl:for-each select="PDFAManagerReport/Validation/Pass">
			<tr>
				<td><xsl:text disable-output-escaping="yes">&lt;a href=&quot;</xsl:text><xsl:value-of select="@FileNameAndPath"/><xsl:text disable-output-escaping="yes">&quot;&gt;</xsl:text><xsl:value-of select="@FileName"/><xsl:text disable-output-escaping="yes">&lt;/a&gt;</xsl:text></td>
			</tr>
		</xsl:for-each>
		</table>
		</div>
 		<h1>PDF/A Revalidation Results (After Conversion):</h1>
		<h2>Run DateTime: <xsl:value-of select="PDFAManagerReport/@RunDateTime"/></h2>
 		<h2>Fail:</h2>
   	<xsl:for-each select="PDFAManagerReport/Revalidation/Fail">
 		  <div style="border: solid darkred 1px;">
 		  <table width="100%">
				<tr>
				  <td><xsl:text disable-output-escaping="yes">&lt;a href=&quot;</xsl:text><xsl:value-of select="@FileNameAndPath"/><xsl:text disable-output-escaping="yes">&quot;&gt;</xsl:text><xsl:value-of select="@FileName"/><xsl:text disable-output-escaping="yes">&lt;/a&gt;</xsl:text></td>
				</tr>
			</table>
			<table width="100%">
			  <tr class="caption">
			    <td width="10%"><I>Error ID</I></td>
			    <td width="70%"><I>Message</I></td>
			    <td width="20%"><I>Obj Refs</I></td>
			  </tr>
			  <xsl:for-each select="Error">
				  <tr>
				    <td><xsl:value-of select="@Code"/></td>
				    <td><xsl:value-of select="@Message"/></td>
				    <td><xsl:value-of select="@Refs"/></td>
				</tr>
			  </xsl:for-each>
			</table>
			</div>
			<br/>
		</xsl:for-each>
 		<h2>Pass:</h2>
	  <div style="border: solid darkblue 1px;">
		<table width="100%">
		<xsl:for-each select="PDFAManagerReport/Revalidation/Pass">
			<tr>
				<td><xsl:text disable-output-escaping="yes">&lt;a href=&quot;</xsl:text><xsl:value-of select="@FileNameAndPath"/><xsl:text disable-output-escaping="yes">&quot;&gt;</xsl:text><xsl:value-of select="@FileName"/><xsl:text disable-output-escaping="yes">&lt;/a&gt;</xsl:text></td>
			</tr>
		</xsl:for-each>
		</table>
		</div>
		<br/>
		<p>Generated using <a target="top" href="http://www.pdftron.com">PDFTron PDF/A Manager 11.3085075</a>.</p>
		</body>
		</html>
	</xsl:template>
</xsl:stylesheet>

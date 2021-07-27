# SalesforceKnowledgeBodyHTML
def get_flattened_meta():
 flattened = dict()
 for m in document.get_meta_data():
   for metadata_name, metadata_values in m.values.iteritems():
    flattened[metadata_name.lower()] = metadata_values
 normalized = dict()
 for metadata_name, metadata_values in flattened.iteritems():
   if len(metadata_values) == 1:
    normalized[metadata_name] = metadata_values[0]
   elif len(metadata_values) > 1:
    normalized[metadata_name] = ';'.join([str(value) for value in metadata_values])
  return normalized

try:
 meta_data = get_flattened_meta()
 bodyHTMLFields = [ 'sftitle', 'sfsummary', 'sfquestion__c', 'sfanswer_id__c', 'sfcontent__c', 'sfdisclaimer__c','sftrademark_plus__c','sffile_attachments__c']
 bodyHTMLLabels = { 'sftitle': 'Title', 'sfsummary': 'Summary', 'sfquestion__c': 'Question','sfanswer_id__c': 'Answer Id', 'sfcontent__c': 'Content', 'sfdisclaimer__c': 'Disclaimer', 'sftrademark_plus__c': 'Trademark Plus','sffile_attachments__c':'Attachment'}
 bodyContentHTML = '<style>.content{}.section{}.section>h2{}</style>'
 bodyContentHTML = bodyContentHTML + '<div class="content">'
 for x in bodyHTMLFields:
  if x in meta_data.keys():
   bodyContentHTML = bodyContentHTML + '<div class="section coveo-cloud-field-label"><h2>' + bodyHTMLLabels[x] + '</h2><span class="coveo-cloud-field-value">' + meta_data[x] + '</span></div>'
 bodyContentHTML = bodyContentHTML + '</div>'
 # log(bodyContentHTML)
 document.add_meta_data({"HasHTMLVersion": True})
 bodyHTMLDataStream = document.DataStream('body_html')
 bodyHTMLDataStream.write(bodyContentHTML.encode('utf8'))
 document.add_data_stream(bodyHTMLDataStream)
except Exception as e:
 log(str(e))
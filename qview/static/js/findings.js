"use strict";

class Findings {
    constructor() {
    }

    init() {
        $('#generate')[0].onclick = update_plots
        $('#documents_all')[0].onclick = documents_select_all
        $('#versions_all')[0].onclick = versions_select_all
        $('#findings_all')[0].onclick = findings_select_all
    }
}

const findings = new Findings()

const update_plots = function () {
    let selected = findings_selected()
}

const findings_selected = function () {
    let documents = $('input.documents:checked')
    let docs = [];
    documents.each(function (i, el) {
        docs.push(documents[i].id)
    });
    let versions = $('input.versions:checked')
    let vers = []
    versions.each(function (i, el) {
        vers.push(versions[i].id)
    });
    return docs, vers
}

const select_all = function () {
    // HACK
    $(this).attr("checked", false)
    $(this).click()
    $(this).attr("checked", true)
}

const documents_select_all = function () {
    $('input.documents').each(select_all)
}

const versions_select_all = function () {
    $('input.versions').each(select_all)
}

const findings_select_all = function () {
    $('input.findings').each(select_all)
}

$(document).ready(function () {
    findings.init()
})

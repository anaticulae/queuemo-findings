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
    let data = findings_selected()

    request('/findings/plots', data, function (response) {
        $('#plots')[0].innerHTML = ''
        response.plots.forEach(function (item) {
            let raw = `<img src="/plots/${item.path}" class="plot"> `
            $('#plots').append(raw)
        })
    })
}

const findings_selected = function () {
    let documents = $.map($('input.documents:checked'), s => s.id)
    let versions = $.map($('input.versions:checked'), s => s.id)
    let findings = $.map($('input.findings:checked'), s => s.id)
    let data = {
        'documents': documents,
        'versions': versions,
        'findings': findings,
    }
    return data
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

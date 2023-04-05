SET FOREIGN_KEY_CHECKS = 0;
INSERT IGNORE INTO callcentermanager.changes_tickets (changes_id, tickets_id)
SELECT changes_id,
    tickets_id
FROM glpi.glpi_changes_tickets;
INSERT IGNORE INTO callcentermanager.groups_tickets (tickets_id, groups_id, type)
SELECT tickets_id,
    groups_id,
    type
FROM glpi.glpi_groups_tickets;
INSERT IGNORE INTO callcentermanager.items_tickets (itemtype, items_id, tickets_id)
SELECT itemtype,
    items_id,
    tickets_id
FROM glpi.glpi_items_tickets;
INSERT IGNORE INTO callcentermanager.olalevels_tickets (tickets_id, olalevels_id, date)
SELECT tickets_id,
    olalevels_id,
    date
FROM glpi.glpi_olalevels_tickets;
INSERT IGNORE INTO callcentermanager.problems_tickets (problems_id, tickets_id)
SELECT problems_id,
    tickets_id
FROM glpi.glpi_problems_tickets;
INSERT IGNORE INTO callcentermanager.projecttasks_tickets (tickets_id, projecttasks_id)
SELECT tickets_id,
    projecttasks_id
FROM glpi.glpi_projecttasks_tickets;
INSERT IGNORE INTO callcentermanager.slalevels_tickets (tickets_id, slalevels_id, date)
SELECT tickets_id,
    slalevels_id,
    date
FROM glpi.glpi_slalevels_tickets;
INSERT IGNORE INTO callcentermanager.suppliers_tickets (
        tickets_id,
        suppliers_id,
        type,
        use_notification,
        alternative_email
    )
SELECT tickets_id,
    suppliers_id,
    type,
    use_notification,
    alternative_email
FROM glpi.glpi_suppliers_tickets;
INSERT IGNORE INTO callcentermanager.ticketcosts (
        tickets_id,
        name,
        comment,
        begin_date,
        end_date,
        actiontime,
        cost_time,
        cost_fixed,
        cost_material,
        budgets_id,
        entities_id
    )
SELECT tickets_id,
    name,
    comment,
    begin_date,
    end_date,
    actiontime,
    cost_time,
    cost_fixed,
    cost_material,
    budgets_id,
    entities_id
FROM glpi.glpi_ticketcosts;
INSERT IGNORE INTO callcentermanager.ticketrecurrents (
        name,
        comment,
        entities_id,
        is_recursive,
        is_active,
        tickettemplates_id,
        begin_date,
        periodicity,
        create_before,
        next_creation_date,
        calendars_id,
        end_date
    )
SELECT name,
    comment,
    entities_id,
    is_recursive,
    is_active,
    tickettemplates_id,
    begin_date,
    periodicity,
    create_before,
    next_creation_date,
    calendars_id,
    end_date
FROM glpi.glpi_ticketrecurrents;
INSERT IGNORE INTO callcentermanager.tickets (
        entities_id,
        name,
        date,
        closedate,
        solvedate,
        date_mod,
        users_id_lastupdater,
        status,
        users_id_recipient,
        requesttypes_id,
        content,
        urgency,
        impact,
        priority,
        itilcategories_id,
        type,
        global_validation,
        slas_id_ttr,
        slas_id_tto,
        slalevels_id_ttr,
        time_to_resolve,
        time_to_own,
        begin_waiting_date,
        sla_waiting_duration,
        ola_waiting_duration,
        olas_id_tto,
        olas_id_ttr,
        olalevels_id_ttr,
        ola_ttr_begin_date,
        internal_time_to_resolve,
        internal_time_to_own,
        waiting_duration,
        close_delay_stat,
        solve_delay_stat,
        takeintoaccount_delay_stat,
        actiontime,
        is_deleted,
        locations_id,
        validation_percent,
        date_creation
    )
SELECT entities_id,
    name,
    date,
    closedate,
    solvedate,
    date_mod,
    users_id_lastupdater,
    status,
    users_id_recipient,
    requesttypes_id,
    content,
    urgency,
    impact,
    priority,
    itilcategories_id,
    type,
    global_validation,
    slas_id_ttr,
    slas_id_tto,
    slalevels_id_ttr,
    time_to_resolve,
    time_to_own,
    begin_waiting_date,
    sla_waiting_duration,
    ola_waiting_duration,
    olas_id_tto,
    olas_id_ttr,
    olalevels_id_ttr,
    ola_ttr_begin_date,
    internal_time_to_resolve,
    internal_time_to_own,
    waiting_duration,
    close_delay_stat,
    solve_delay_stat,
    takeintoaccount_delay_stat,
    actiontime,
    is_deleted,
    locations_id,
    validation_percent,
    date_creation
FROM glpi.glpi_tickets;
INSERT IGNORE INTO callcentermanager.tickets_contracts (tickets_id, contracts_id)
SELECT tickets_id,
    contracts_id
FROM glpi.glpi_tickets_contracts;
INSERT IGNORE INTO callcentermanager.tickets_tickets (tickets_id_1, tickets_id_2, link)
SELECT tickets_id_1,
    tickets_id_2,
    link
FROM glpi.glpi_tickets_tickets;
INSERT IGNORE INTO callcentermanager.tickets_users (
        tickets_id,
        users_id,
        type,
        use_notification,
        alternative_email
    )
SELECT tickets_id,
    users_id,
    type,
    use_notification,
    alternative_email
FROM glpi.glpi_tickets_users;
INSERT IGNORE INTO callcentermanager.ticketsatisfactions (
        tickets_id,
        type,
        date_begin,
        date_answered,
        satisfaction,
        comment
    )
SELECT tickets_id,
    type,
    date_begin,
    date_answered,
    satisfaction,
    comment
FROM glpi.glpi_ticketsatisfactions;
INSERT IGNORE INTO callcentermanager.tickettasks (
        uuid,
        tickets_id,
        taskcategories_id,
        date,
        users_id,
        users_id_editor,
        content,
        is_private,
        actiontime,
        begin,
    end,
    state,
    users_id_tech,
    groups_id_tech,
    date_mod,
    date_creation,
    tasktemplates_id,
    timeline_position,
    sourceitems_id,
    sourceof_items_id
)
SELECT uuid,
    tickets_id,
    taskcategories_id,
    date,
    users_id,
    users_id_editor,
    content,
    is_private,
    actiontime,
    begin,
end,
state,
users_id_tech,
groups_id_tech,
date_mod,
date_creation,
tasktemplates_id,
timeline_position,
sourceitems_id,
sourceof_items_id
FROM glpi.glpi_tickettasks;
INSERT IGNORE INTO callcentermanager.tickettemplatehiddenfields (tickettemplates_id, num)
SELECT tickettemplates_id,
    num
FROM glpi.glpi_tickettemplatehiddenfields;
INSERT IGNORE INTO callcentermanager.tickettemplatemandatoryfields (tickettemplates_id, num)
SELECT tickettemplates_id,
    num
FROM glpi.glpi_tickettemplatemandatoryfields;
INSERT IGNORE INTO callcentermanager.tickettemplatepredefinedfields (tickettemplates_id, num, value)
SELECT tickettemplates_id,
    num,
    value
FROM glpi.glpi_tickettemplatepredefinedfields;
INSERT IGNORE INTO callcentermanager.tickettemplates (name, entities_id, is_recursive, comment)
SELECT name,
    entities_id,
    is_recursive,
    comment
FROM glpi.glpi_tickettemplates;
INSERT IGNORE INTO callcentermanager.ticketvalidations (
        entities_id,
        users_id,
        tickets_id,
        users_id_validate,
        comment_submission,
        comment_validation,
        status,
        submission_date,
        validation_date,
        timeline_position
    )
SELECT entities_id,
    users_id,
    tickets_id,
    users_id_validate,
    comment_submission,
    comment_validation,
    status,
    submission_date,
    validation_date,
    timeline_position
FROM glpi.glpi_ticketvalidations;
INSERT IGNORE INTO callcentermanager.logs (
        itemtype,
        items_id,
        itemtype_link,
        linked_action,
        user_name,
        date_mod,
        id_search_option,
        old_value,
        new_value
    )
SELECT itemtype,
    items_id,
    itemtype_link,
    linked_action,
    user_name,
    date_mod,
    id_search_option,
    old_value,
    new_value
FROM glpi.glpi_logs;
INSERT IGNORE INTO callcentermanager.events (items_id, type, date, service, level, message)
SELECT items_id,
    type,
    date,
    service,
    level,
    message
FROM glpi.glpi_events;
INSERT IGNORE INTO callcentermanager.agents (
        deviceid,
        entities_id,
        is_recursive,
        name,
        agenttypes_id,
        last_contact,
        version,
        locked,
        itemtype,
        items_id,
        useragent,
        tag,
        port,
        threads_networkdiscovery,
        threads_networkinventory,
        timeout_networkdiscovery,
        timeout_networkinventory
    )
SELECT deviceid,
    entities_id,
    is_recursive,
    name,
    agenttypes_id,
    last_contact,
    version,
    locked,
    itemtype,
    items_id,
    useragent,
    tag,
    port,
    threads_networkdiscovery,
    threads_networkinventory,
    timeout_networkdiscovery,
    timeout_networkinventory
FROM glpi.glpi_agents;
INSERT IGNORE INTO callcentermanager.domains (
        name,
        entities_id,
        is_recursive,
        domaintypes_id,
        date_expiration,
        date_domaincreation,
        users_id_tech,
        groups_id_tech,
        is_deleted,
        comment,
        is_template,
        template_name,
        is_active,
        date_mod,
        date_creation
    )
SELECT name,
    entities_id,
    is_recursive,
    domaintypes_id,
    date_expiration,
    date_domaincreation,
    users_id_tech,
    groups_id_tech,
    is_deleted,
    comment,
    is_template,
    template_name,
    is_active,
    date_mod,
    date_creation
FROM glpi.glpi_domains;
INSERT IGNORE INTO callcentermanager.calendars (
        name,
        entities_id,
        is_recursive,
        comment,
        date_mod,
        cache_duration,
        date_creation
    )
SELECT name,
    entities_id,
    is_recursive,
    comment,
    date_mod,
    cache_duration,
    date_creation
FROM glpi.glpi_calendars;
INSERT IGNORE INTO callcentermanager.recurrentchanges (
        name,
        comment,
        entities_id,
        is_recursive,
        is_active,
        changetemplates_id,
        begin_date,
        periodicity,
        create_before,
        next_creation_date,
        calendars_id,
        end_date
    )
SELECT name,
    comment,
    entities_id,
    is_recursive,
    is_active,
    changetemplates_id,
    begin_date,
    periodicity,
    create_before,
    next_creation_date,
    calendars_id,
    end_date
FROM glpi.glpi_recurrentchanges;
INSERT IGNORE INTO callcentermanager.changes_users (
        changes_id,
        users_id,
        type,
        use_notification,
        alternative_email
    )
SELECT changes_id,
    users_id,
    type,
    use_notification,
    alternative_email
FROM glpi.glpi_changes_users;
INSERT IGNORE INTO callcentermanager.changes (
        name,
        entities_id,
        is_recursive,
        is_deleted,
        status,
        content,
        date_mod,
        date,
        solvedate,
        closedate,
        time_to_resolve,
        users_id_recipient,
        users_id_lastupdater,
        urgency,
        impact,
        priority,
        itilcategories_id,
        impactcontent,
        controlistcontent,
        rolloutplancontent,
        backoutplancontent,
        checklistcontent,
        global_validation,
        validation_percent,
        actiontime,
        begin_waiting_date,
        waiting_duration,
        close_delay_stat,
        solve_delay_stat,
        date_creation
    )
SELECT name,
    entities_id,
    is_recursive,
    is_deleted,
    status,
    content,
    date_mod,
    date,
    solvedate,
    closedate,
    time_to_resolve,
    users_id_recipient,
    users_id_lastupdater,
    urgency,
    impact,
    priority,
    itilcategories_id,
    impactcontent,
    controlistcontent,
    rolloutplancontent,
    backoutplancontent,
    checklistcontent,
    global_validation,
    validation_percent,
    actiontime,
    begin_waiting_date,
    waiting_duration,
    close_delay_stat,
    solve_delay_stat,
    date_creation
FROM glpi.glpi_changes;
INSERT IGNORE INTO callcentermanager.groups_knowbaseitems (
        knowbaseitems_id,
        groups_id,
        entities_id,
        is_recursive,
        no_entity_restriction
    )
SELECT knowbaseitems_id,
    groups_id,
    entities_id,
    is_recursive,
    no_entity_restriction
FROM glpi.glpi_groups_knowbaseitems;
INSERT IGNORE INTO callcentermanager.groups_problems (problems_id, groups_id, type)
SELECT problems_id,
    groups_id,
    type
FROM glpi.glpi_groups_problems;
INSERT IGNORE INTO callcentermanager.groups_reminders (
        reminders_id,
        groups_id,
        entities_id,
        is_recursive,
        no_entity_restriction
    )
SELECT reminders_id,
    groups_id,
    entities_id,
    is_recursive,
    no_entity_restriction
FROM glpi.glpi_groups_reminders;
INSERT IGNORE INTO callcentermanager.groups_rssfeeds (
        rssfeeds_id,
        groups_id,
        entities_id,
        is_recursive,
        no_entity_restriction
    )
SELECT rssfeeds_id,
    groups_id,
    entities_id,
    is_recursive,
    no_entity_restriction
FROM glpi.glpi_groups_rssfeeds;
INSERT IGNORE INTO callcentermanager.groups_users (
        users_id,
        groups_id,
        is_dynamic,
        is_manager,
        is_userdelegate
    )
SELECT users_id,
    groups_id,
    is_dynamic,
    is_manager,
    is_userdelegate
FROM glpi.glpi_groups_users;
INSERT IGNORE INTO callcentermanager.problems (
        name,
        entities_id,
        is_recursive,
        is_deleted,
        status,
        content,
        date_mod,
        date,
        solvedate,
        closedate,
        time_to_resolve,
        users_id_recipient,
        users_id_lastupdater,
        urgency,
        impact,
        priority,
        itilcategories_id,
        impactcontent,
        causecontent,
        symptomcontent,
        actiontime,
        begin_waiting_date,
        waiting_duration,
        close_delay_stat,
        solve_delay_stat,
        date_creation
    )
SELECT name,
    entities_id,
    is_recursive,
    is_deleted,
    status,
    content,
    date_mod,
    date,
    solvedate,
    closedate,
    time_to_resolve,
    users_id_recipient,
    users_id_lastupdater,
    urgency,
    impact,
    priority,
    itilcategories_id,
    impactcontent,
    causecontent,
    symptomcontent,
    actiontime,
    begin_waiting_date,
    waiting_duration,
    close_delay_stat,
    solve_delay_stat,
    date_creation
FROM glpi.glpi_problems;
INSERT IGNORE INTO callcentermanager.problems_users (
        problems_id,
        users_id,
        type,
        use_notification,
        alternative_email
    )
SELECT problems_id,
    users_id,
    type,
    use_notification,
    alternative_email
FROM glpi.glpi_problems_users;
INSERT IGNORE INTO callcentermanager.planningexternalevents (
        uuid,
        planningexternaleventtemplates_id,
        entities_id,
        is_recursive,
        date,
        users_id,
        users_id_guests,
        groups_id,
        name,
        text,
        begin,
    end,
    rrule,
    state,
    planningeventcategories_id,
    background,
    date_mod,
    date_creation
)
SELECT uuid,
    planningexternaleventtemplates_id,
    entities_id,
    is_recursive,
    date,
    users_id,
    users_id_guests,
    groups_id,
    name,
    text,
    begin,
end,
rrule,
state,
planningeventcategories_id,
background,
date_mod,
date_creation
FROM glpi.glpi_planningexternalevents;
INSERT IGNORE INTO callcentermanager.planningexternaleventtemplates (
        entities_id,
        name,
        text,
        comment,
        duration,
        before_time,
        rrule,
        state,
        planningeventcategories_id,
        background,
        date_mod,
        date_creation
    )
SELECT entities_id,
    name,
    text,
    comment,
    duration,
    before_time,
    rrule,
    state,
    planningeventcategories_id,
    background,
    date_mod,
    date_creation
FROM glpi.glpi_planningexternaleventtemplates;
INSERT IGNORE INTO callcentermanager.planningrecalls (
        items_id,
        itemtype,
        users_id,
        before_time,
        `when`
    )
SELECT items_id,
    itemtype,
    users_id,
    before_time,
    `when`
FROM glpi.glpi_planningrecalls;
INSERT IGNORE INTO callcentermanager.planningeventcategories (name, color, comment, date_mod, date_creation)
SELECT name,
    color,
    comment,
    date_mod,
    date_creation
FROM glpi.glpi_planningeventcategories;
INSERT IGNORE INTO callcentermanager.crontasklogs (
        crontasks_id,
        crontasklogs_id,
        date,
        state,
        elapsed,
        volume,
        content
    )
SELECT crontasks_id,
    crontasklogs_id,
    date,
    state,
    elapsed,
    volume,
    content
FROM glpi.glpi_crontasklogs;
INSERT IGNORE INTO callcentermanager.crontasks (
        itemtype,
        name,
        frequency,
        param,
        state,
        mode,
        allowmode,
        hourmin,
        hourmax,
        logs_lifetime,
        lastrun,
        lastcode,
        comment,
        date_mod,
        date_creation
    )
SELECT itemtype,
    name,
    frequency,
    param,
    state,
    mode,
    allowmode,
    hourmin,
    hourmax,
    logs_lifetime,
    lastrun,
    lastcode,
    comment,
    date_mod,
    date_creation
FROM glpi.glpi_crontasks;
INSERT IGNORE INTO callcentermanager.autoupdatesystems (name, comment)
SELECT name,
    comment
FROM glpi.glpi_autoupdatesystems;
INSERT IGNORE INTO callcentermanager.manufacturers (name, comment, date_mod, date_creation)
SELECT name,
    comment,
    date_mod,
    date_creation
FROM glpi.glpi_manufacturers;
INSERT IGNORE INTO callcentermanager.operatingsystems (name, comment, date_mod, date_creation)
SELECT name,
    comment,
    date_mod,
    date_creation
FROM glpi.glpi_operatingsystems;
INSERT IGNORE INTO callcentermanager.networks (name, comment, date_mod, date_creation)
SELECT name,
    comment,
    date_mod,
    date_creation
FROM glpi.glpi_networks;
INSERT IGNORE INTO callcentermanager.snmpcredentials (
        name,
        snmpversion,
        community,
        username,
        authentication,
        auth_passphrase,
        encryption,
        priv_passphrase,
        is_deleted
    )
SELECT name,
    snmpversion,
    community,
    username,
    authentication,
    auth_passphrase,
    encryption,
    priv_passphrase,
    is_deleted
FROM glpi.glpi_snmpcredentials;
INSERT IGNORE INTO callcentermanager.authldaps (
        name,
        host,
        basedn,
        rootdn,
        port,
        `condition`,
        login_field,
        sync_field,
        use_tls,
        group_field,
        group_condition,
        group_search_type,
        group_member_field,
        email1_field,
        realname_field,
        firstname_field,
        phone_field,
        phone2_field,
        mobile_field,
        comment_field,
        use_dn,
        time_offset,
        deref_option,
        title_field,
        category_field,
        language_field,
        entity_field,
        entity_condition,
        date_mod,
        comment,
        is_default,
        is_active,
        rootdn_passwd,
        registration_number_field,
        email2_field,
        email3_field,
        email4_field,
        location_field,
        responsible_field,
        pagesize,
        ldap_maxlimit,
        can_support_pagesize,
        picture_field,
        date_creation,
        inventory_domain,
        tls_certfile,
        tls_keyfile,
        use_bind,
        timeout
    )
SELECT name,
    host,
    basedn,
    rootdn,
    port,
    `condition`,
    login_field,
    sync_field,
    use_tls,
    group_field,
    group_condition,
    group_search_type,
    group_member_field,
    email1_field,
    realname_field,
    firstname_field,
    phone_field,
    phone2_field,
    mobile_field,
    comment_field,
    use_dn,
    time_offset,
    deref_option,
    title_field,
    category_field,
    language_field,
    entity_field,
    entity_condition,
    date_mod,
    comment,
    is_default,
    is_active,
    rootdn_passwd,
    registration_number_field,
    email2_field,
    email3_field,
    email4_field,
    location_field,
    responsible_field,
    pagesize,
    ldap_maxlimit,
    can_support_pagesize,
    picture_field,
    date_creation,
    inventory_domain,
    tls_certfile,
    tls_keyfile,
    use_bind,
    timeout
FROM glpi.glpi_authldaps;
INSERT IGNORE INTO callcentermanager.entities (
        name,
        completename,
        comment,
        level,
        sons_cache,
        ancestors_cache,
        registration_number,
        address,
        postcode,
        town,
        state,
        country,
        website,
        phonenumber,
        fax,
        email,
        admin_email,
        admin_email_name,
        from_email,
        from_email_name,
        noreply_email,
        noreply_email_name,
        replyto_email,
        replyto_email_name,
        notification_subject_tag,
        ldap_dn,
        tag,
        mail_domain,
        entity_ldapfilter,
        mailing_signature,
        cartridges_alert_repeat,
        consumables_alert_repeat,
        use_licenses_alert,
        send_licenses_alert_before_delay,
        use_certificates_alert,
        send_certificates_alert_before_delay,
        certificates_alert_repeat_interval,
        use_contracts_alert,
        send_contracts_alert_before_delay,
        use_infocoms_alert,
        send_infocoms_alert_before_delay,
        use_reservations_alert,
        use_domains_alert,
        send_domains_alert_close_expiries_delay,
        send_domains_alert_expired_delay,
        autoclose_delay,
        autopurge_delay,
        notclosed_delay,
        calendars_strategy,
        auto_assign_mode,
        tickettype,
        max_closedate,
        inquest_config,
        inquest_rate,
        inquest_delay,
        inquest_URL,
        autofill_warranty_date,
        autofill_use_date,
        autofill_buy_date,
        autofill_delivery_date,
        autofill_order_date,
        tickettemplates_strategy,
        changetemplates_strategy,
        changetemplates,
        problemtemplates_strategy,
        problemtemplates,
        entities_strategy_software,
        entities_software,
        default_contract_alert,
        default_infocom_alert,
        default_cartridges_alarm_threshold,
        delay_send_emails,
        is_notif_enable_default,
        inquest_duration,
        date_mod,
        date_creation,
        autofill_decommission_date,
        suppliers_as_private,
        anonymize_support_agents,
        display_users_initials,
        contracts_strategy_default,
        contracts_default,
        enable_custom_css,
        custom_css_code,
        latitude,
        longitude,
        altitude,
        transfers_strategy,
        transfers,
        agent_base_url,
        authldaps_id,
        calendars_id,
        entities_id,
        tickettemplates_id
    )
SELECT name,
    completename,
    comment,
    level,
    sons_cache,
    ancestors_cache,
    registration_number,
    address,
    postcode,
    town,
    state,
    country,
    website,
    phonenumber,
    fax,
    email,
    admin_email,
    admin_email_name,
    from_email,
    from_email_name,
    noreply_email,
    noreply_email_name,
    replyto_email,
    replyto_email_name,
    notification_subject_tag,
    ldap_dn,
    tag,
    mail_domain,
    entity_ldapfilter,
    mailing_signature,
    cartridges_alert_repeat,
    consumables_alert_repeat,
    use_licenses_alert,
    send_licenses_alert_before_delay,
    use_certificates_alert,
    send_certificates_alert_before_delay,
    certificates_alert_repeat_interval,
    use_contracts_alert,
    send_contracts_alert_before_delay,
    use_infocoms_alert,
    send_infocoms_alert_before_delay,
    use_reservations_alert,
    use_domains_alert,
    send_domains_alert_close_expiries_delay,
    send_domains_alert_expired_delay,
    autoclose_delay,
    autopurge_delay,
    notclosed_delay,
    calendars_strategy,
    auto_assign_mode,
    tickettype,
    max_closedate,
    inquest_config,
    inquest_rate,
    inquest_delay,
    inquest_URL,
    autofill_warranty_date,
    autofill_use_date,
    autofill_buy_date,
    autofill_delivery_date,
    autofill_order_date,
    tickettemplates_strategy,
    changetemplates_strategy,
    changetemplates_id,
    problemtemplates_strategy,
    problemtemplates_id,
    entities_strategy_software,
    entities_id_software,
    default_contract_alert,
    default_infocom_alert,
    default_cartridges_alarm_threshold,
    delay_send_emails,
    is_notif_enable_default,
    inquest_duration,
    date_mod,
    date_creation,
    autofill_decommission_date,
    suppliers_as_private,
    anonymize_support_agents,
    display_users_initials,
    contracts_strategy_default,
    contracts_id_default,
    enable_custom_css,
    custom_css_code,
    latitude,
    longitude,
    altitude,
    transfers_strategy,
    transfers_id,
    agent_base_url,
    authldaps_id,
    calendars_id,
    entities_id,
    tickettemplates_id
FROM glpi.glpi_entities;
INSERT IGNORE INTO callcentermanager.locations (
        is_recursive,
        name,
        completename,
        comment,
        level,
        ancestors_cache,
        sons_cache,
        address,
        postcode,
        town,
        state,
        country,
        building,
        room,
        latitude,
        longitude,
        altitude,
        date_mod,
        date_creation,
        entities_id,
        locations_id
    )
SELECT is_recursive,
    name,
    completename,
    comment,
    level,
    ancestors_cache,
    sons_cache,
    address,
    postcode,
    town,
    state,
    country,
    building,
    room,
    latitude,
    longitude,
    altitude,
    date_mod,
    date_creation,
    entities_id,
    locations_id
FROM glpi.glpi_locations;
INSERT IGNORE INTO callcentermanager.states (
        name,
        is_recursive,
        comment,
        completename,
        level,
        ancestors_cache,
        sons_cache,
        is_visible_computer,
        is_visible_monitor,
        is_visible_networkequipment,
        is_visible_peripheral,
        is_visible_phone,
        is_visible_printer,
        is_visible_softwareversion,
        is_visible_softwarelicense,
        is_visible_line,
        is_visible_certificate,
        is_visible_rack,
        is_visible_passivedcequipment,
        is_visible_enclosure,
        is_visible_pdu,
        is_visible_cluster,
        is_visible_contract,
        is_visible_appliance,
        is_visible_databaseinstance,
        is_visible_cable,
        date_mod,
        date_creation,
        entities_id,
        states_id
    )
SELECT name,
    is_recursive,
    comment,
    completename,
    level,
    ancestors_cache,
    sons_cache,
    is_visible_computer,
    is_visible_monitor,
    is_visible_networkequipment,
    is_visible_peripheral,
    is_visible_phone,
    is_visible_printer,
    is_visible_softwareversion,
    is_visible_softwarelicense,
    is_visible_line,
    is_visible_certificate,
    is_visible_rack,
    is_visible_passivedcequipment,
    is_visible_enclosure,
    is_visible_pdu,
    is_visible_cluster,
    is_visible_contract,
    is_visible_appliance,
    is_visible_databaseinstance,
    is_visible_cable,
    date_mod,
    date_creation,
    entities_id,
    states_id
FROM glpi.glpi_states;
INSERT IGNORE INTO callcentermanager.softwarecategories (
        name,
        comment,
        completename,
        level,
        ancestors_cache,
        sons_cache,
        softwarecategories_id
    )
SELECT name,
    comment,
    completename,
    level,
    ancestors_cache,
    sons_cache,
    softwarecategories_id
FROM glpi.glpi_softwarecategories;
INSERT IGNORE INTO callcentermanager.softwares (
        is_recursive,
        name,
        comment,
        is_update,
        is_deleted,
        is_template,
        template_name,
        date_mod,
        ticket_tco,
        is_helpdesk_visible,
        is_valid,
        date_creation,
        pictures,
        entities_id,
        groups_id,
        groups_tech_id,
        locations_id,
        manufacturers_id,
        softwarecategories_id,
        softwares_id,
        users_id,
        users_tech_id
    )
SELECT is_recursive,
    name,
    comment,
    is_update,
    is_deleted,
    is_template,
    template_name,
    date_mod,
    ticket_tco,
    is_helpdesk_visible,
    is_valid,
    date_creation,
    pictures,
    entities_id,
    groups_id,
    groups_id_tech,
    locations_id,
    manufacturers_id,
    softwarecategories_id,
    softwares_id,
    users_id,
    users_id_tech
FROM glpi.glpi_softwares;
INSERT IGNORE INTO callcentermanager.networkequipmentmodels (
        name,
        comment,
        product_number,
        weight,
        required_units,
        depth,
        power_connections,
        power_consumption,
        is_half_rack,
        picture_front,
        picture_rear,
        pictures,
        date_mod
    )
SELECT name,
    comment,
    product_number,
    weight,
    required_units,
    depth,
    power_connections,
    power_consumption,
    is_half_rack,
    picture_front,
    picture_rear,
    pictures,
    date_mod
FROM glpi.glpi_networkequipmentmodels;
INSERT IGNORE INTO callcentermanager.networkequipmenttypes ()
SELECT *
FROM glpi.glpi_networkequipmenttypes;
INSERT IGNORE INTO callcentermanager.networkequipments (is_recursive, name, ram, serial, otherserial, contact, contact_num, date_mod, comment, is_deleted, is_template, template_name, ticket_tco, is_dynamic, uuid, date_creation, sysdescr, cpu, uptime, last_inventory_update, autoupdatesystems_id, entities_id, groups_id, groups_tech_id, locations_id, manufacturers_id, networkequipmentmodels_id, networkequipmenttypes_id, networks_id, snmpcredentials_id, states_id, users_id, users_tech_id)
SELECT is_recursive, name, ram, serial, otherserial, contact, contact_num, date_mod, comment, is_deleted, is_template, template_name, ticket_tco, is_dynamic, uuid, date_creation, sysdescr, cpu, uptime, last_inventory_update, autoupdatesystems_id, entities_id, groups_id, groups_id_tech, locations_id, manufacturers_id, networkequipmentmodels_id, networkequipmenttypes_id, networks_id, snmpcredentials_id, states_id, users_id, users_id_tech
FROM glpi.glpi_networkequipments;
INSERT IGNORE INTO callcentermanager.printermodels ()
SELECT *
FROM glpi.glpi_printermodels;
INSERT IGNORE INTO callcentermanager.printertypes ()
SELECT *
FROM glpi.glpi_printertypes;
INSERT IGNORE INTO callcentermanager.printers (is_recursive, name, date_mod, contact, contact_num, serial, otherserial, have_serial, have_parallel, have_usb, have_wifi, have_ethernet, comment, memory_size, is_global, is_deleted, is_template, template_name, init_pages_counter, last_pages_counter, ticket_tco, is_dynamic, uuid, date_creation, sysdescr, last_inventory_update, autoupdatesystems_id, entities_id, groups_id, groups_tech_id, locations_id, manufacturers_id, networks_id, printermodels_id, printertypes_id, snmpcredentials_id, states_id, users_id, users_tech_id)
SELECT is_recursive, name, date_mod, contact, contact_num, serial, otherserial, have_serial, have_parallel, have_usb, have_wifi, have_ethernet, comment, memory_size, is_global, is_deleted, is_template, template_name, init_pages_counter, last_pages_counter, ticket_tco, is_dynamic, uuid, date_creation, sysdescr, last_inventory_update, autoupdatesystems_id, entities_id, groups_id, groups_id_tech, locations_id, manufacturers_id, networks_id, printermodels_id, printertypes_id, snmpcredentials_id, states_id, users_id, users_id_tech
FROM glpi.glpi_printers;
INSERT IGNORE INTO callcentermanager.cartridgeitems (is_recursive, name, ref, is_deleted, comment, alarm_threshold, stock_target, date_mod, date_creation, pictures, cartridgeitemtypes_id, entities_id, groups_tech_id, locations_id, manufacturers_id, users_tech_id)
SELECT is_recursive, name, ref, is_deleted, comment, alarm_threshold, stock_target, date_mod, date_creation, pictures, cartridgeitemtypes_id, entities_id, groups_id_tech, locations_id, manufacturers_id, users_id_tech
FROM glpi.glpi_cartridgeitems;
INSERT IGNORE INTO callcentermanager.cartridges ()
SELECT *
FROM glpi.glpi_cartridges;
INSERT IGNORE INTO callcentermanager.rackmodels ()
SELECT *
FROM glpi.glpi_rackmodels;
INSERT IGNORE INTO callcentermanager.racktypes ()
SELECT *
FROM glpi.glpi_racktypes;
INSERT IGNORE INTO callcentermanager.consumableitemtypes ()
SELECT *
FROM glpi.glpi_consumableitemtypes;
INSERT IGNORE INTO callcentermanager.consumableitems (
        is_recursive,
        name,
        ref,
        is_deleted,
        comment,
        alarm_threshold,
        stock_target,
        date_mod,
        date_creation,
        otherserial,
        pictures,
        consumableitemtypes_id,
        entities_id,
        groups_tech_id,
        locations_id,
        manufacturers_id,
        users_tech_id
    )
SELECT is_recursive,
    name,
    ref,
    is_deleted,
    comment,
    alarm_threshold,
    stock_target,
    date_mod,
    date_creation,
    otherserial,
    pictures,
    consumableitemtypes_id,
    entities_id,
    groups_id_tech,
    locations_id,
    manufacturers_id,
    users_id_tech
FROM glpi.glpi_consumableitems;
INSERT IGNORE INTO callcentermanager.consumables ()
SELECT *
FROM glpi.glpi_consumables;
INSERT IGNORE INTO callcentermanager.datacenters ()
SELECT *
FROM glpi.glpi_datacenters;
INSERT IGNORE INTO callcentermanager.dcrooms ()
SELECT *
FROM glpi.glpi_dcrooms;
INSERT IGNORE INTO callcentermanager.racks (name, comment, is_recursive, serial, otherserial, width, height, depth, number_units, is_template, template_name, is_deleted, room_orientation, position, bgcolor, max_power, mesured_power, max_weight, date_creation, dcrooms_id, entities_id, groups_tech_id, locations_id, manufacturers_id, rackmodels_id, racktypes_id, states_id, users_tech_id)
SELECT name, comment, is_recursive, serial, otherserial, width, height, depth, number_units, is_template, template_name, is_deleted, room_orientation, position, bgcolor, max_power, mesured_power, max_weight, date_creation, dcrooms_id, entities_id, groups_id_tech, locations_id, manufacturers_id, rackmodels_id, racktypes_id, states_id, users_id_tech
FROM glpi.glpi_racks;
INSERT IGNORE INTO callcentermanager.enclosuremodels ()
SELECT *
FROM glpi.glpi_enclosuremodels;
INSERT IGNORE INTO callcentermanager.enclosures (name, is_recursive, serial, otherserial, is_template, template_name, orientation, power_supplies, comment, is_deleted, date_mod, date_creation, enclosuremodels_id, entities_id, groups_tech_id, locations_id, manufacturers_id, states_id, users_tech_id)
SELECT name, is_recursive, serial, otherserial, is_template, template_name, orientation, power_supplies, comment, is_deleted, date_mod, date_creation, enclosuremodels_id, entities_id, groups_id_tech, locations_id, manufacturers_id, states_id, users_id_tech
FROM glpi.glpi_enclosures;
INSERT IGNORE INTO callcentermanager.pdutypes ()
SELECT *
FROM glpi.glpi_pdutypes;
INSERT IGNORE INTO callcentermanager.pdumodels ()
SELECT *
FROM glpi.glpi_pdumodels;
INSERT IGNORE INTO callcentermanager.pdus (name, is_recursive, serial, otherserial, is_template, template_name, comment, is_deleted, date_mod, date_creation, entities_id, locations_id, manufacturers_id, pdumodels_id, pdutypes_id, states_id)
SELECT name, is_recursive, serial, otherserial, is_template, template_name, comment, is_deleted, date_mod, date_creation, entities_id, locations_id, manufacturers_id, pdumodels_id, pdutypes_id, states_id
FROM glpi.glpi_pdus;
INSERT IGNORE INTO callcentermanager.unmanageds (
        is_recursive,
        name,
        serial,
        otherserial,
        contact,
        contact_num,
        date_mod,
        comment,
        is_deleted,
        is_dynamic,
        date_creation,
        sysdescr,
        itemtype,
        accepted,
        hub,
        ip,
        agents_id,
        autoupdatesystems_id,
        domains_id,
        entities_id,
        groups_id,
        locations_id,
        manufacturers_id,
        networks_id,
        snmpcredentials_id,
        states_id,
        users_id
    )
SELECT is_recursive,
    name,
    serial,
    otherserial,
    contact,
    contact_num,
    date_mod,
    comment,
    is_deleted,
    is_dynamic,
    date_creation,
    sysdescr,
    itemtype,
    accepted,
    hub,
    ip,
    agents_id,
    autoupdatesystems_id,
    domains_id,
    entities_id,
    groups_id,
    locations_id,
    manufacturers_id,
    networks_id,
    snmpcredentials_id,
    states_id,
    users_id
FROM glpi.glpi_unmanageds;
INSERT IGNORE INTO callcentermanager.socketmodels ()
SELECT *
FROM glpi.glpi_socketmodels;
INSERT IGNORE INTO callcentermanager.networkports ()
SELECT *
FROM glpi.glpi_networkports;
INSERT IGNORE INTO callcentermanager.sockets ()
SELECT *
FROM glpi.glpi_sockets;
INSERT IGNORE INTO callcentermanager.cablestrands ()
SELECT *
FROM glpi.glpi_cablestrands;
INSERT IGNORE INTO callcentermanager.cabletypes ()
SELECT *
FROM glpi.glpi_cabletypes;
INSERT IGNORE INTO callcentermanager.cables (
        name,
        is_recursive,
        itemtype_endpoint_a,
        itemtype_endpoint_b,
        color,
        otherserial,
        comment,
        date_mod,
        date_creation,
        cablestrands_id,
        cabletypes_id,
        entities_id,
        items_endpoint_a_id,
        items_endpoint_b_id,
        socketmodels_endpoint_a_id,
        socketmodels_endpoint_b_id,
        sockets_endpoint_a_id,
        sockets_endpoint_b_id,
        states_id,
        users_tech_id
    )
SELECT name,
    is_recursive,
    itemtype_endpoint_a,
    itemtype_endpoint_b,
    color,
    otherserial,
    comment,
    date_mod,
    date_creation,
    cablestrands_id,
    cabletypes_id,
    entities_id,
    items_id_endpoint_a,
    items_id_endpoint_b,
    socketmodels_id_endpoint_a,
    socketmodels_id_endpoint_b,
    sockets_id_endpoint_a,
    sockets_id_endpoint_b,
    states_id,
    users_id_tech
FROM glpi.glpi_cables;
INSERT IGNORE INTO callcentermanager.devicesimcardtypes ()
SELECT *
FROM glpi.glpi_devicesimcardtypes;
INSERT IGNORE INTO callcentermanager.devicesimcards (
        designation,
        comment,
        entities_id,
        is_recursive,
        manufacturers_id,
        voltage,
        devicesimcardtypes_id,
        date_mod,
        date_creation,
        allow_voip
    )
SELECT designation,
    comment,
    entities_id,
    is_recursive,
    manufacturers_id,
    voltage,
    devicesimcardtypes_id,
    date_mod,
    date_creation,
    allow_voip
FROM glpi.glpi_devicesimcards;
INSERT IGNORE INTO callcentermanager.computermodels ()
SELECT *
FROM glpi.glpi_computermodels;
INSERT IGNORE INTO callcentermanager.computertypes ()
SELECT *
FROM glpi.glpi_computertypes;
INSERT IGNORE INTO callcentermanager.monitormodels ()
SELECT *
FROM glpi.glpi_monitormodels;
INSERT IGNORE INTO callcentermanager.monitortypes ()
SELECT *
FROM glpi.glpi_monitortypes;
INSERT IGNORE INTO callcentermanager.softwarelicensetypes ()
SELECT *
FROM glpi.glpi_softwarelicensetypes;
INSERT IGNORE INTO callcentermanager.softwareversions ()
SELECT *
FROM glpi.glpi_softwareversions;
INSERT IGNORE INTO callcentermanager.softwarelicenses ()
SELECT *
FROM glpi.glpi_softwarelicenses;
INSERT IGNORE INTO callcentermanager.printers_cartridgeinfos ()
SELECT *
FROM glpi.glpi_printers_cartridgeinfos;
INSERT IGNORE INTO callcentermanager.cartridgeitemtypes ()
SELECT *
FROM glpi.glpi_cartridgeitemtypes;
INSERT IGNORE INTO callcentermanager.cartridgeitems_printermodels ()
SELECT *
FROM glpi.glpi_cartridgeitems_printermodels;
INSERT IGNORE INTO callcentermanager.cartridgeitems_printermodels ()
SELECT *
FROM glpi.glpi_cartridgeitems_printermodels;
INSERT IGNORE INTO callcentermanager.phonemodels ()
SELECT *
FROM glpi.glpi_phonemodels;
INSERT IGNORE INTO callcentermanager.phonepowersupplies ()
SELECT *
FROM glpi.glpi_phonepowersupplies;
INSERT IGNORE INTO callcentermanager.phonetypes ()
SELECT *
FROM glpi.glpi_phonetypes;
INSERT IGNORE INTO callcentermanager.phones (name, date_mod, contact, contact_num, comment, serial, otherserial, brand, number_line, have_headset, have_hp, is_global, is_deleted, is_template, template_name, ticket_tco, is_dynamic, uuid, date_creation, is_recursive, last_inventory_update, autoupdatesystems_id, entities_id, groups_id, groups_tech_id, locations_id, manufacturers_id, phonemodels_id, phonepowersupplies_id, phonetypes_id, states_id, users_id, users_tech_id)
SELECT name, date_mod, contact, contact_num, comment, serial, otherserial, brand, number_line, have_headset, have_hp, is_global, is_deleted, is_template, template_name, ticket_tco, is_dynamic, uuid, date_creation, is_recursive, last_inventory_update, autoupdatesystems_id, entities_id, groups_id, groups_id_tech, locations_id, manufacturers_id, phonemodels_id, phonepowersupplies_id, phonetypes_id, states_id, users_id, users_id_tech
FROM glpi.glpi_phones;
INSERT IGNORE INTO callcentermanager.items_racks ()
SELECT *
FROM glpi.glpi_items_racks;
INSERT IGNORE INTO callcentermanager.items_enclosures ()
SELECT *
FROM glpi.glpi_items_enclosures;
INSERT IGNORE INTO callcentermanager.plugs ()
SELECT *
FROM glpi.glpi_plugs;
INSERT IGNORE INTO callcentermanager.pdus_plugs ()
SELECT *
FROM glpi.glpi_pdus_plugs;
INSERT IGNORE INTO callcentermanager.pdus_racks ()
SELECT *
FROM glpi.glpi_pdus_racks;
INSERT IGNORE INTO callcentermanager.devicebatterytypes ()
SELECT *
FROM glpi.glpi_devicebatterytypes;
INSERT IGNORE INTO callcentermanager.devicebatterymodels ()
SELECT *
FROM glpi.glpi_devicebatterymodels;
INSERT IGNORE INTO callcentermanager.devicebatteries (
        designation,
        comment,
        manufacturers_id,
        voltage,
        capacity,
        devicebatterytypes_id,
        entities_id,
        is_recursive,
        devicebatterymodels_id,
        date_mod,
        date_creation
    )
SELECT designation,
    comment,
    manufacturers_id,
    voltage,
    capacity,
    devicebatterytypes_id,
    entities_id,
    is_recursive,
    devicebatterymodels_id,
    date_mod,
    date_creation
FROM glpi.glpi_devicebatteries;
INSERT IGNORE INTO callcentermanager.devicecameramodels ()
SELECT *
FROM glpi.glpi_devicecameramodels;
INSERT IGNORE INTO callcentermanager.devicecameras (
        designation,
        flashunit,
        lensfacing,
        orientation,
        focallength,
        sensorsize,
        comment,
        manufacturers_id,
        entities_id,
        is_recursive,
        devicecameramodels_id,
        support,
        date_mod,
        date_creation
    )
SELECT designation,
    flashunit,
    lensfacing,
    orientation,
    focallength,
    sensorsize,
    comment,
    manufacturers_id,
    entities_id,
    is_recursive,
    devicecameramodels_id,
    support,
    date_mod,
    date_creation
FROM glpi.glpi_devicecameras;
INSERT IGNORE INTO callcentermanager.devicecasemodels ()
SELECT *
FROM glpi.glpi_devicecasemodels;
INSERT IGNORE INTO callcentermanager.devicecasetypes ()
SELECT *
FROM glpi.glpi_devicecasetypes;
INSERT IGNORE INTO callcentermanager.devicecases (
        designation,
        devicecasetypes_id,
        comment,
        manufacturers_id,
        entities_id,
        is_recursive,
        devicecasemodels_id,
        date_mod,
        date_creation
    )
SELECT designation,
    devicecasetypes_id,
    comment,
    manufacturers_id,
    entities_id,
    is_recursive,
    devicecasemodels_id,
    date_mod,
    date_creation
FROM glpi.glpi_devicecases;
INSERT IGNORE INTO callcentermanager.devicecontrolmodels ()
SELECT *
FROM glpi.glpi_devicecontrolmodels;
INSERT IGNORE INTO callcentermanager.interfacetypes ()
SELECT *
FROM glpi.glpi_interfacetypes;
INSERT IGNORE INTO callcentermanager.devicecontrols (
        designation,
        is_raid,
        comment,
        manufacturers_id,
        interfacetypes_id,
        entities_id,
        is_recursive,
        devicecontrolmodels_id,
        date_mod,
        date_creation
    )
SELECT designation,
    is_raid,
    comment,
    manufacturers_id,
    interfacetypes_id,
    entities_id,
    is_recursive,
    devicecontrolmodels_id,
    date_mod,
    date_creation
FROM glpi.glpi_devicecontrols;
INSERT IGNORE INTO callcentermanager.devicedrivemodels ()
SELECT *
FROM glpi.glpi_devicedrivemodels;
INSERT IGNORE INTO callcentermanager.devicedrives (
        designation,
        is_writer,
        speed,
        comment,
        manufacturers_id,
        interfacetypes_id,
        entities_id,
        is_recursive,
        devicedrivemodels_id,
        date_mod,
        date_creation
    )
SELECT designation,
    is_writer,
    speed,
    comment,
    manufacturers_id,
    interfacetypes_id,
    entities_id,
    is_recursive,
    devicedrivemodels_id,
    date_mod,
    date_creation
FROM glpi.glpi_devicedrives;
INSERT IGNORE INTO callcentermanager.devicefirmwaremodels ()
SELECT *
FROM glpi.glpi_devicefirmwaremodels;
INSERT IGNORE INTO callcentermanager.devicefirmwaretypes ()
SELECT *
FROM glpi.glpi_devicefirmwaretypes;
INSERT IGNORE INTO callcentermanager.devicefirmwares (
        designation,
        comment,
        manufacturers_id,
        date,
        version,
        devicefirmwaretypes_id,
        entities_id,
        is_recursive,
        devicefirmwaremodels_id,
        date_mod,
        date_creation
    )
SELECT designation,
    comment,
    manufacturers_id,
    date,
    version,
    devicefirmwaretypes_id,
    entities_id,
    is_recursive,
    devicefirmwaremodels_id,
    date_mod,
    date_creation
FROM glpi.glpi_devicefirmwares;
INSERT IGNORE INTO callcentermanager.devicegenericmodels ()
SELECT *
FROM glpi.glpi_devicegenericmodels;
INSERT IGNORE INTO callcentermanager.devicegenerictypes ()
SELECT *
FROM glpi.glpi_devicegenerictypes;
INSERT IGNORE INTO callcentermanager.devicegenerics (
        designation,
        devicegenerictypes_id,
        comment,
        manufacturers_id,
        entities_id,
        is_recursive,
        locations_id,
        states_id,
        devicegenericmodels_id,
        date_mod,
        date_creation
    )
SELECT designation,
    devicegenerictypes_id,
    comment,
    manufacturers_id,
    entities_id,
    is_recursive,
    locations_id,
    states_id,
    devicegenericmodels_id,
    date_mod,
    date_creation
FROM glpi.glpi_devicegenerics;
INSERT IGNORE INTO callcentermanager.devicegraphiccardmodels ()
SELECT *
FROM glpi.glpi_devicegraphiccardmodels;
INSERT IGNORE INTO callcentermanager.devicegraphiccards (
        designation,
        interfacetypes_id,
        comment,
        manufacturers_id,
        memory_default,
        entities_id,
        is_recursive,
        devicegraphiccardmodels_id,
        chipset,
        date_mod,
        date_creation
    )
SELECT designation,
    interfacetypes_id,
    comment,
    manufacturers_id,
    memory_default,
    entities_id,
    is_recursive,
    devicegraphiccardmodels_id,
    chipset,
    date_mod,
    date_creation
FROM glpi.glpi_devicegraphiccards;
INSERT IGNORE INTO callcentermanager.deviceharddrivemodels ()
SELECT *
FROM glpi.glpi_deviceharddrivemodels;
INSERT IGNORE INTO callcentermanager.deviceharddrives (
        designation,
        rpm,
        interfacetypes_id,
        cache,
        comment,
        manufacturers_id,
        capacity_default,
        entities_id,
        is_recursive,
        deviceharddrivemodels_id,
        date_mod,
        date_creation
    )
SELECT designation,
    rpm,
    interfacetypes_id,
    cache,
    comment,
    manufacturers_id,
    capacity_default,
    entities_id,
    is_recursive,
    deviceharddrivemodels_id,
    date_mod,
    date_creation
FROM glpi.glpi_deviceharddrives;
INSERT IGNORE INTO callcentermanager.devicememorymodels ()
SELECT *
FROM glpi.glpi_devicememorymodels;
INSERT IGNORE INTO callcentermanager.devicememorytypes ()
SELECT *
FROM glpi.glpi_devicememorytypes;
INSERT IGNORE INTO callcentermanager.devicememories (
        designation,
        frequence,
        comment,
        size_default,
        is_recursive,
        date_mod,
        date_creation,
        devicememorymodels_id,
        devicememorytypes_id,
        entities_id,
        manufacturers_id
    )
SELECT designation,
    frequence,
    comment,
    size_default,
    is_recursive,
    date_mod,
    date_creation,
    devicememorymodels_id,
    devicememorytypes_id,
    entities_id,
    manufacturers_id
FROM glpi.glpi_devicememories;
INSERT IGNORE INTO callcentermanager.peripheralmodels ()
SELECT *
FROM glpi.glpi_peripheralmodels;
INSERT IGNORE INTO callcentermanager.peripheraltypes ()
SELECT *
FROM glpi.glpi_peripheraltypes;
INSERT IGNORE INTO callcentermanager.peripherals (name, date_mod, contact, contact_num, comment, serial, otherserial, brand, is_deleted, is_global, is_template, template_name, ticket_tco, is_dynamic, uuid, date_creation, is_recursive, autoupdatesystems_id, entities_id, groups_id, groups_tech_id, locations_id, manufacturers_id, peripheralmodels_id, peripheraltypes_id, states_id, users_id, users_tech_id)
SELECT name, date_mod, contact, contact_num, comment, serial, otherserial, brand, is_deleted, is_global, is_template, template_name, ticket_tco, is_dynamic, uuid, date_creation, is_recursive, autoupdatesystems_id, entities_id, groups_id, groups_id_tech, locations_id, manufacturers_id, peripheralmodels_id, peripheraltypes_id, states_id, users_id, users_id_tech
FROM glpi.glpi_peripherals;
INSERT IGNORE INTO callcentermanager.devicemotherboardmodels ()
SELECT *
FROM glpi.glpi_devicemotherboardmodels;
INSERT IGNORE INTO callcentermanager.devicemotherboards (
        designation,
        chipset,
        comment,
        manufacturers_id,
        entities_id,
        is_recursive,
        devicemotherboardmodels_id,
        date_mod,
        date_creation
    )
SELECT designation,
    chipset,
    comment,
    manufacturers_id,
    entities_id,
    is_recursive,
    devicemotherboardmodels_id,
    date_mod,
    date_creation
FROM glpi.glpi_devicemotherboards;
INSERT IGNORE INTO callcentermanager.devicenetworkcardmodels ()
SELECT *
FROM glpi.glpi_devicenetworkcardmodels;
INSERT IGNORE INTO callcentermanager.devicenetworkcards (
        designation,
        bandwidth,
        comment,
        manufacturers_id,
        mac_default,
        entities_id,
        is_recursive,
        devicenetworkcardmodels_id,
        date_mod,
        date_creation
    )
SELECT designation,
    bandwidth,
    comment,
    manufacturers_id,
    mac_default,
    entities_id,
    is_recursive,
    devicenetworkcardmodels_id,
    date_mod,
    date_creation
FROM glpi.glpi_devicenetworkcards;
INSERT IGNORE INTO callcentermanager.devicepcimodels ()
SELECT *
FROM glpi.glpi_devicepcimodels;
INSERT IGNORE INTO callcentermanager.devicepcis (
        designation,
        comment,
        manufacturers_id,
        devicenetworkcardmodels_id,
        entities_id,
        is_recursive,
        devicepcimodels_id,
        date_mod,
        date_creation
    )
SELECT designation,
    comment,
    manufacturers_id,
    devicenetworkcardmodels_id,
    entities_id,
    is_recursive,
    devicepcimodels_id,
    date_mod,
    date_creation
FROM glpi.glpi_devicepcis;
INSERT IGNORE INTO callcentermanager.devicepowersupplymodels ()
SELECT *
FROM glpi.glpi_devicepowersupplymodels;
INSERT IGNORE INTO callcentermanager.deviceprocessormodels ()
SELECT *
FROM glpi.glpi_deviceprocessormodels;
INSERT IGNORE INTO callcentermanager.devicepowersupplies (
        designation,
        power,
        is_atx,
        comment,
        manufacturers_id,
        entities_id,
        is_recursive,
        devicepowersupplymodels_id,
        date_mod,
        date_creation
    )
SELECT designation,
    power,
    is_atx,
    comment,
    manufacturers_id,
    entities_id,
    is_recursive,
    devicepowersupplymodels_id,
    date_mod,
    date_creation
FROM glpi.glpi_devicepowersupplies;
INSERT IGNORE INTO callcentermanager.deviceprocessors (
        designation,
        frequence,
        comment,
        manufacturers_id,
        frequency_default,
        nbcores_default,
        nbthreads_default,
        entities_id,
        is_recursive,
        deviceprocessormodels_id,
        date_mod,
        date_creation
    )
SELECT designation,
    frequence,
    comment,
    manufacturers_id,
    frequency_default,
    nbcores_default,
    nbthreads_default,
    entities_id,
    is_recursive,
    deviceprocessormodels_id,
    date_mod,
    date_creation
FROM glpi.glpi_deviceprocessors;
INSERT IGNORE INTO callcentermanager.devicesensormodels ()
SELECT *
FROM glpi.glpi_devicesensormodels;
INSERT IGNORE INTO callcentermanager.devicesensortypes ()
SELECT *
FROM glpi.glpi_devicesensortypes;
INSERT IGNORE INTO callcentermanager.devicesensors (
        designation,
        devicesensortypes_id,
        devicesensormodels_id,
        comment,
        manufacturers_id,
        entities_id,
        is_recursive,
        locations_id,
        states_id,
        date_mod,
        date_creation
    )
SELECT designation,
    devicesensortypes_id,
    devicesensormodels_id,
    comment,
    manufacturers_id,
    entities_id,
    is_recursive,
    locations_id,
    states_id,
    date_mod,
    date_creation
FROM glpi.glpi_devicesensors;
INSERT IGNORE INTO callcentermanager.devicesoundcardmodels ()
SELECT *
FROM glpi.glpi_devicesoundcardmodels;
INSERT IGNORE INTO callcentermanager.devicesoundcards (
        designation,
        type,
        comment,
        manufacturers_id,
        entities_id,
        is_recursive,
        devicesoundcardmodels_id,
        date_mod,
        date_creation
    )
SELECT designation,
    type,
    comment,
    manufacturers_id,
    entities_id,
    is_recursive,
    devicesoundcardmodels_id,
    date_mod,
    date_creation
FROM glpi.glpi_devicesoundcards;
INSERT IGNORE INTO callcentermanager.items_devicebatteries ()
SELECT *
FROM glpi.glpi_items_devicebatteries;
INSERT IGNORE INTO callcentermanager.items_devicecameras ()
SELECT *
FROM glpi.glpi_items_devicecameras;
INSERT IGNORE INTO callcentermanager.imageformats ()
SELECT *
FROM glpi.glpi_imageformats;
INSERT IGNORE INTO callcentermanager.imageresolutions ()
SELECT *
FROM glpi.glpi_imageresolutions;
INSERT IGNORE INTO callcentermanager.items_devicecameras_imageformats (
        item_devicecameras_id,
        imageformats_id,
        is_dynamic
    )
SELECT item_devicecameras_id,
    imageformats_id,
    is_dynamic
FROM glpi.glpi_items_devicecameras_imageformats;
INSERT IGNORE INTO callcentermanager.items_devicecameras_imageresolutions (
        item_devicecameras_id,
        imageresolutions_id,
        is_dynamic
    )
SELECT item_devicecameras_id,
    imageresolutions_id,
    is_dynamic
FROM glpi.glpi_items_devicecameras_imageresolutions;
INSERT IGNORE INTO callcentermanager.items_devicecases ()
SELECT *
FROM glpi.glpi_items_devicecases;
INSERT IGNORE INTO callcentermanager.items_devicecontrols ()
SELECT *
FROM glpi.glpi_items_devicecontrols;
INSERT IGNORE INTO callcentermanager.items_devicedrives ()
SELECT *
FROM glpi.glpi_items_devicedrives;
INSERT IGNORE INTO callcentermanager.items_devicefirmwares ()
SELECT *
FROM glpi.glpi_items_devicefirmwares;
INSERT IGNORE INTO callcentermanager.items_devicegenerics ()
SELECT *
FROM glpi.glpi_items_devicegenerics;
INSERT IGNORE INTO callcentermanager.items_devicegraphiccards ()
SELECT *
FROM glpi.glpi_items_devicegraphiccards;
INSERT IGNORE INTO callcentermanager.items_deviceharddrives ()
SELECT *
FROM glpi.glpi_items_deviceharddrives;
INSERT IGNORE INTO callcentermanager.items_devicememories ()
SELECT *
FROM glpi.glpi_items_devicememories;
INSERT IGNORE INTO callcentermanager.items_devicemotherboards ()
SELECT *
FROM glpi.glpi_items_devicemotherboards;
INSERT IGNORE INTO callcentermanager.items_devicenetworkcards ()
SELECT *
FROM glpi.glpi_items_devicenetworkcards;
INSERT IGNORE INTO callcentermanager.items_devicepcis ()
SELECT *
FROM glpi.glpi_items_devicepcis;
INSERT IGNORE INTO callcentermanager.items_devicepowersupplies ()
SELECT *
FROM glpi.glpi_items_devicepowersupplies;
INSERT IGNORE INTO callcentermanager.items_deviceprocessors ()
SELECT *
FROM glpi.glpi_items_deviceprocessors;
INSERT IGNORE INTO callcentermanager.items_devicesensors ()
SELECT *
FROM glpi.glpi_items_devicesensors;
INSERT IGNORE INTO callcentermanager.linetypes ()
SELECT *
FROM glpi.glpi_linetypes;
INSERT IGNORE INTO callcentermanager.lineoperators ()
SELECT *
FROM glpi.glpi_lineoperators;
INSERT IGNORE INTO callcentermanager.lines ()
SELECT *
FROM glpi.glpi_lines;
INSERT IGNORE INTO callcentermanager.items_devicesimcards (
        items_id,
        itemtype,
        devicesimcards_id,
        is_deleted,
        is_dynamic,
        entities_id,
        is_recursive,
        serial,
        otherserial,
        states_id,
        locations_id,
        lines_id,
        users_id,
        groups_id,
        pin,
        pin2,
        puk,
        puk2,
        msin
    )
SELECT items_id,
    itemtype,
    devicesimcards_id,
    is_deleted,
    is_dynamic,
    entities_id,
    is_recursive,
    serial,
    otherserial,
    states_id,
    locations_id,
    lines_id,
    users_id,
    groups_id,
    pin,
    pin2,
    puk,
    puk2,
    msin
FROM glpi.glpi_items_devicesimcards;
INSERT IGNORE INTO callcentermanager.items_devicesoundcards ()
SELECT *
FROM glpi.glpi_items_devicesoundcards;
INSERT IGNORE INTO callcentermanager.passivedcequipmentmodels ()
SELECT *
FROM glpi.glpi_passivedcequipmentmodels;
INSERT IGNORE INTO callcentermanager.passivedcequipmenttypes ()
SELECT *
FROM glpi.glpi_passivedcequipmenttypes;
INSERT IGNORE INTO callcentermanager.passivedcequipments (
        name,
        is_recursive,
        serial,
        otherserial,
        is_template,
        template_name,
        comment,
        is_deleted,
        date_mod,
        date_creation,
        entities_id,
        groups_tech_id,
        locations_id,
        manufacturers_id,
        passivedcequipmentmodels_id,
        passivedcequipmenttypes_id,
        states_id,
        users_tech_id
    )
SELECT name,
    is_recursive,
    serial,
    otherserial,
    is_template,
    template_name,
    comment,
    is_deleted,
    date_mod,
    date_creation,
    entities_id,
    groups_id_tech,
    locations_id,
    manufacturers_id,
    passivedcequipmentmodels_id,
    passivedcequipmenttypes_id,
    states_id,
    users_id_tech
FROM glpi.glpi_passivedcequipments;
INSERT IGNORE INTO callcentermanager.entities_knowbaseitems ()
SELECT *
FROM glpi.glpi_entities_knowbaseitems;
INSERT IGNORE INTO callcentermanager.entities_reminders ()
SELECT *
FROM glpi.glpi_entities_reminders;
INSERT IGNORE INTO callcentermanager.entities_rssfeeds ()
SELECT *
FROM glpi.glpi_entities_rssfeeds;
INSERT IGNORE INTO callcentermanager.fqdns ()
SELECT *
FROM glpi.glpi_fqdns;
INSERT IGNORE INTO callcentermanager.networknames ()
SELECT *
FROM glpi.glpi_networknames;
INSERT IGNORE INTO callcentermanager.networkaliases ()
SELECT *
FROM glpi.glpi_networkaliases;
INSERT IGNORE INTO callcentermanager.networkinterfaces ()
SELECT *
FROM glpi.glpi_networkinterfaces;
INSERT IGNORE INTO callcentermanager.networkportaggregates ()
SELECT *
FROM glpi.glpi_networkportaggregates;
INSERT IGNORE INTO callcentermanager.networkportaliases ()
SELECT *
FROM glpi.glpi_networkportaliases;
INSERT IGNORE INTO callcentermanager.networkportconnectionlogs ()
SELECT *
FROM glpi.glpi_networkportconnectionlogs;
INSERT IGNORE INTO callcentermanager.networkportdialups ()
SELECT *
FROM glpi.glpi_networkportdialups;
INSERT IGNORE INTO callcentermanager.networkportethernets ()
SELECT *
FROM glpi.glpi_networkportethernets;
INSERT IGNORE INTO callcentermanager.networkportfiberchanneltypes ()
SELECT *
FROM glpi.glpi_networkportfiberchanneltypes;
INSERT IGNORE INTO callcentermanager.networkportfiberchannels ()
SELECT *
FROM glpi.glpi_networkportfiberchannels;
INSERT IGNORE INTO callcentermanager.networkportlocals ()
SELECT *
FROM glpi.glpi_networkportlocals;
INSERT IGNORE INTO callcentermanager.networkportmetrics ()
SELECT *
FROM glpi.glpi_networkportmetrics;
INSERT IGNORE INTO callcentermanager.networkports_networkports ()
SELECT *
FROM glpi.glpi_networkports_networkports;
INSERT IGNORE INTO callcentermanager.vlans ()
SELECT *
FROM glpi.glpi_vlans;
INSERT IGNORE INTO callcentermanager.networkports_vlans ()
SELECT *
FROM glpi.glpi_networkports_vlans;
INSERT IGNORE INTO callcentermanager.networkporttypes ()
SELECT *
FROM glpi.glpi_networkporttypes;
INSERT IGNORE INTO callcentermanager.networkportwifis ()
SELECT *
FROM glpi.glpi_networkportwifis;
INSERT IGNORE INTO callcentermanager.computers (
        entities_id,
        name,
        serial,
        otherserial,
        contact,
        contact_num,
        users_tech_id,
        groups_tech_id,
        comment,
        date_mod,
        autoupdatesystems_id,
        locations_id,
        networks_id,
        computermodels_id,
        computertypes_id,
        is_template,
        template_name,
        manufacturers_id,
        is_deleted,
        is_dynamic,
        users_id,
        groups_id,
        states_id,
        ticket_tco,
        uuid,
        date_creation,
        is_recursive,
        last_inventory_update
    )
SELECT entities_id,
    name,
    serial,
    otherserial,
    contact,
    contact_num,
    users_id_tech,
    groups_id_tech,
    comment,
    date_mod,
    autoupdatesystems_id,
    locations_id,
    networks_id,
    computermodels_id,
    computertypes_id,
    is_template,
    template_name,
    manufacturers_id,
    is_deleted,
    is_dynamic,
    users_id,
    groups_id,
    states_id,
    ticket_tco,
    uuid,
    date_creation,
    is_recursive,
    last_inventory_update
FROM glpi.glpi_computers;
INSERT IGNORE INTO callcentermanager.monitors (name, date_mod, contact, contact_num, comment, serial, otherserial, size, have_micro, have_speaker, have_subd, have_bnc, have_pivot, have_hdmi, have_displayport, is_deleted, is_global, is_template, template_name, ticket_tco, is_dynamic, uuid, date_creation, is_recursive, autoupdatesystems_id, entities_id, groups_id, groups_tech_id, locations_id, manufacturers_id, monitormodels_id, monitortypes_id, states_id, users_id)
SELECT name, date_mod, contact, contact_num, comment, serial, otherserial, size, have_micro, have_speaker, have_subd, have_bnc, have_pivot, have_hdmi, have_displayport, is_deleted, is_global, is_template, template_name, ticket_tco, is_dynamic, uuid, date_creation, is_recursive, autoupdatesystems_id, entities_id, groups_id, groups_id_tech, locations_id, manufacturers_id, monitormodels_id, monitortypes_id, states_id, users_id
FROM glpi.glpi_monitors;
INSERT IGNORE INTO callcentermanager.computers_items ()
SELECT *
FROM glpi.glpi_computers_items;
INSERT IGNORE INTO callcentermanager.items_operatingsystems (items_id, itemtype, operatingsystems_id, operatingsystemversions_id, operatingsystemservicepacks_id, operatingsystemarchitectures_id, operatingsystemkernelversions_id, license_number, licenseid, operatingsystemeditions_id, date_mod, date_creation, is_deleted, is_dynamic, entities_id, is_recursive)
SELECT items_id, itemtype, operatingsystems_id, operatingsystemversions_id, operatingsystemservicepacks_id, operatingsystemarchitectures_id, operatingsystemkernelversions_id, license_number, licenseid, operatingsystemeditions_id, date_mod, date_creation, is_deleted, is_dynamic, entities_id, is_recursive
FROM glpi.glpi_items_operatingsystems;